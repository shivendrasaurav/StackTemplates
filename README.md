# Stack Templates for Popular Tech Stacks

Welcome to the Stack Templates repository! 🚀 This project aims to provide ready-to-use templates for various popular technology stacks, making it easier for developers to kickstart their projects with best practices and common configurations already in place.

## Available Templates

Currently, we offer the following templates:

1. `react-w-router`: React with Vite app initialized with React Router and Patterns UI by Invrz
2. `fastapi-postgres`: FastAPI initialized with Router and a Microservice with PostgreSQL Connection

## How to Use These Templates

To use a template, you'll need to add this repository as a remote to your local Git repository and then pull the specific branch containing the template you want. Here's a step-by-step guide:

### 1. Create a New Local Repository

First, create a new directory for your project and initialize it as a Git repository:

```bash
mkdir my-new-project
cd my-new-project
git init
```

### 2. Add This Repository as a Remote

Add this Stack Templates repository as a remote to your local repository:

```bash
git remote add template https://github.com/shivendrasaurav/StackTemplates.git
```

### 3. Fetch the Remote Branches

Fetch all the branches from the template repository:

```bash
git fetch template
```

### 4. Pull the Desired Template

Choose the template you want to use and pull it into your local repository. Replace `<branch-name>` with the name of the template branch you want (e.g., `react-w-router` or `fastapi-postgres`):

```bash
git pull template <branch-name>
```

For example, to pull the React with Router template:

```bash
git pull template react-w-router
```

### 5. Remove the Template Remote (Optional)

If you don't plan to pull any more templates, you can remove the template remote:

```bash
git remote remove template
```

### 6. Start Working on Your Project

You now have the template code in your local repository. You can start modifying it to suit your project needs.

## Template-Specific Instructions

Each template has its own README file with specific instructions for setup, configuration, and usage. After pulling a template, make sure to read its README for detailed information.

## Contributing

We welcome contributions to improve existing templates or add new ones! If you have ideas for new templates or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please open an issue in this repository, and we'll be glad to help!

---

Happy coding! 🎉