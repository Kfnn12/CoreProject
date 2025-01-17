<!-- https://github.com/baseplate-admin/CoreProject/blob/django-patch/backend/django_core/apps/user/templates/user/signup.html -->
<script lang="ts">
    import reporter from "@felte/reporter-tippy";
    import { validator } from "@felte/validator-yup";
    import { createForm } from "felte";
    import voca from "voca";
    import * as yup from "yup";

    import { goto } from "$app/navigation";
    import { UrlMaps } from "$data/urls";

    const urls = new UrlMaps();
    // Creating yup schema
    const schema = yup.object({
        username: yup
            ?.string()
            ?.required("Please Enter User Name")
            ?.min(0)
            ?.max(50, "User name must be less than 50 Characters"),
        email: yup?.string()?.email("Enter a valid Email")?.required("Please Enter Email"),
        password: yup
            ?.string()
            ?.min(8, "Password must be more than 8 Characters")
            ?.matches(
                /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/,
                "Must Contain 8 Characters, One Uppercase, One Lowercase, One Number and one special case Character"
            )
            ?.max(1024, "Password must be less than 1024 Characters"),
        confirm_password: yup
            ?.string()
            ?.oneOf(
                [yup.ref("password"), null],
                "<b>Confirm Password</b> and <b>Password</b> are not the same"
            )
    });
    // Creating the form
    const { form, errors } = createForm({
        initialValues: {
            username: "",
            email: "",
            password: "",
            confirm_password: ""
        },
        onSubmit: async (values) => {
            const data = new FormData();
            data.append("username", values.username);
            data.append("email", values.email);
            data.append("password", values.password);

            const res = await fetch(urls.signup(), {
                method: "POST",
                body: data
            });

            if (res.ok) {
                goto("./login");
            }
        },
        // onSuccess(response, context) {
        // 	// Do something with the returned value from `onSubmit`.
        // },
        // onError(err, context) {
        // 	// Do something with the error thrown from `onSubmit`.
        // },
        extend: [
            validator({ schema }),
            reporter({
                tippyProps: {
                    allowHTML: true
                }
            })
        ],

        // Debounced async validation
        debounced: {
            timeout: 300,
            validate: async (values) => {
                const warnings: Partial<typeof values> = {};
                // Check for username availability
                if (values.username) {
                    const valueRegex = values.username.match(/#/gi);
                    if (!valueRegex) {
                        return;
                    }

                    const HashLength = valueRegex.length;
                    // Remove Empty Elements
                    const splittedValue = values.username.split("#").filter((i) => i);

                    if (
                        HashLength === 1 &&
                        splittedValue.length === 2 &&
                        !isNaN(Number(splittedValue[1]))
                    ) {
                        let formData = new FormData();
                        formData.append("username", splittedValue[0] ?? "");
                        formData.append(
                            "discriminator",
                            voca.padLeft(splittedValue[1], 4, "0") ?? ""
                        );

                        const res = await fetch(urls.username_validity(), {
                            method: "POST",
                            body: formData
                        });
                        if (res.status === 302) {
                            // The username with discriminator is taken by another user
                            // Show an error
                            warnings["username"] = "This username is not available";
                        } else if (res.status === 404) {
                            // ok
                        }
                    } else if (HashLength >= 1) {
                        warnings["username"] =
                            "There must be one hash in the username. ( eg: SoraAmamiya#1993 )";
                    } else if (isNaN(Number(splittedValue[1]))) {
                        warnings["username"] =
                            "The discriminator must be a number. ( eg : SoraAmamiya#1993 )";
                    }
                }
                return warnings;
            }
        }
    });
    const input_mapping = [
        {
            type: "text",
            placeholder: "Username",
            name: "username"
        },
        {
            type: "email",
            placeholder: "Email",
            name: "email"
        },
        {
            type: "password",
            placeholder: "Password",
            name: "password"
        },
        {
            type: "password",
            placeholder: "Confirm Password",
            name: "confirm_password"
        }
    ];
</script>

<svelte:head>
    <title>CoreProject | Sign Up</title>
</svelte:head>

<form use:form>
    <div class="grid gap-6">
        {#each input_mapping as input_item}
            <input
                style="--tw-bg-opacity:0.30"
                type={input_item.type}
                placeholder={input_item.placeholder}
                name={input_item.name}
                class="input h-16 border-[3px] border-warning font-semibold text-white placeholder:uppercase focus:outline-0"
            />
        {/each}
    </div>
    <div class="mt-10 flex items-center justify-center gap-2">
        <button
            class="btn-secondary btn font-bold text-black"
            type="submit"
        >
            Register
        </button>
        or
        <a
            class="link"
            href="./login"
        >
            login
        </a>
    </div>
</form>
