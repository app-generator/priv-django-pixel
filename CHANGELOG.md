# Change Log

## [1.0.18] 2025-04-11
### Changes

- Update README Links (minor)

## [1.0.17] 2025-02-13
### Changes

- Bump UI Version: `v1.0.7`

## [1.0.16] 2025-02-13
### Changes

- Bump UI Version
- Update DEMO Link - [Django Pixel](https://django-pixel.onrender.com/) 

## [1.0.15] 2025-02-08
### Changes

- Update Templates Folder
- Customize the HOMEpage

## [1.0.14] 2024-12-16
### Changes

- Preselect the design in the Generator:
  - [Django App Generator - Pixel UI KIT](https://app-generator.dev/tools/django-generator/pixel/)
- (Optional) Design Database: edit models and fields
- (Optional) Edit the fields for the extended user model
- (Optional) Enable OAuth for GitHub
- (Optional) Add Celery (async tasks)
- (Optional) Enable Dynamic API Module
- Docker Scripts
- Render CI/Cd Scripts

**The generated Django project is available as a ZIP Archive and also uploaded to GitHub.**

## [1.0.13] 2024-11-29
### Changes

> Update RM Links

- 👉 [Django Pixel](https://app-generator.dev/product/pixel-bootstrap/django/) - `Product Page`
- 👉 [Django Pixel Documentation](https://app-generator.dev/docs/products/django/pixel/index.html) - `Complete Information` and Support Links
  - [Getting Started with Django](https://app-generator.dev/docs/technologies/django/index.html) - a `comprehensive tutorial`
  - `Configuration`: Install Tailwind/Flowbite, Prepare Environment, Setting up the Database 
  - `Start with Docker`
  - `Manual Build`
  - `Start the project`
  - `Deploy on Render`

## [1.0.12] 2024-05-18
### Changes

- Updated DOCS (readme)
  - [Custom Development](https://appseed.us/custom-development/) Section
  - [CI/CD Assistance for AWS, DO](https://appseed.us/terms/#section-ci-cd)

## [1.0.11] 2024-03-05
### Changes

- Deprecate `distutils`
  - use `str2bool`
- Update Deps 
  - `requirements.txt` 
- Update [Custom Development](https://appseed.us/custom-development/) Section
  - New Pricing: `$3,999`

## [1.0.10] 2023-10-24
### Changes

- Update Dependencies 
- Update README 

## [1.0.9] 2023-02-09
### Changes

- Bump UI: [Django Theme Pixel](https://github.com/app-generator/django-theme-pixel) `v1.0.3`
- DOCS Update (readme). New sections:
  - `How to customize the theme`
  - Render deployment
- Configure the project to use `home/templates`
- Added `custom-index` sample
- `Fix Docker` Execution
  - `Update Settings`: ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS `sections`

## [1.0.8] 2023-01-10
### Changes

- Move to theme-based pattern
  - [Django Theme Pixel](https://github.com/app-generator/django-theme-pixel)
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

## [1.0.7] 2022-05-30
### Improvements

- Built with [Pixel Lite Generator](https://appseed.us/generator/pixel-bootstrap/)
  - Timestamp: `2022-05-31 08:05`

## [1.0.6] 2022-01-17
### Improvements

- Bump Django Codebase to [v2.0.0](https://github.com/app-generator/boilerplate-code-django/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## [1.0.5] 2021-12-08
### Improvements 

- Bump Django Codebase to [v1.0.7](https://github.com/app-generator/boilerplate-code-django/releases)

## [1.0.4] 2021-09-07
### Improvements & Fixes

- Bump Django Codebase to [v1.0.5](https://github.com/app-generator/boilerplate-code-django/releases)
  - Dependencies update (all packages)
  - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update 
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.3] 2021-07-18
### Tooling

- Added scripts to recompile the SCSS files
    - `core/static/assets/` - gulpfile.js
    - `core/static/assets/` - package.json
- `Update README` - [Recompile SCSS](https://github.com/app-generator/django-pixel-lite#recompile-css) (new section)

## [1.0.2] 2021-05-21
### Improvements

- Bump UI: [Jinja Pixel Lite](https://github.com/app-generator/jinja-pixel-lite) v1.0.2 / Pixel Lite v4.0.0
- Codebase: [Django Boilerplate](https://github.com/app-generator/boilerplate-code-django) v1.0.4

## [1.0.1] 2021-01-12
### Improvements

- Bump UI: [Pixel Lite](https://github.com/themesberg/pixel-bootstrap-ui-kit) v3.1.2
- Codebase: [Django Boilerplate](https://github.com/app-generator/boilerplate-code-django) v1.0.4

## [1.0.0] 2020-09-20
### Initial Release

