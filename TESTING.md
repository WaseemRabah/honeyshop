# Main Testing Focus

Each page's functionality and behavior were tested under different user roles. Here are the main areas of focus:

## Navbar:

The Navbar features were thoroughly tested to ensure functionality and usability:

- Logo navigation was tested to redirect users to the home page.
- Navigation links to different pages were checked to ensure proper redirection.
- Sort selector functionality on product pages was tested.
- Search functionality was tested for accurate product search results.

![Logo](documentation/logo-image.png)

![All Products List](documentation/all-products-list-image.png)

![All Products](documentation/all-products-image.png)

![Raw Honey](documentation/rawhoney-image.png)

![Raw Honey Products](documentation/rawhoney-products-image.png)

![Pure Honey](documentation/purehoney-image.png)

![Pure Honey Products](documentation/purehoney-products-image.png)

![Special Offers](documentation/specialoffers-image.png)

![Special Offers Products](documentation/specialoffers-products-image.png)

## Home Page:

- Delivery Banner and Hero Section functionality were tested for proper display.
- Shop Now button functionality was verified to redirect users to the products page.

![Home page](documentation/main-image.png)

![Shop Now Button](documentation/shop-now-button.png)

![Shop Now Products](documentation/shop-now-products.png)



## Footer:

- Newletter Subscription feature was tested for successful subscription.
- Success and error messages were verified for the newsletter subscription process.

![Footer](documentation/footer-image.png)

![Newsletter](documentation/newsletter-image.png)

## Sign Up:

- User registration and sign-up process were tested for accurate data capture.
- Email verification process was validated, including confirmation email receipt and account activation.

![Sign Up](documentation/signup-form-image.png)

![verification](documentation/verification-image.png)

## Sign In:

- User login functionality was tested for successful authentication.
- Error handling for incorrect login credentials was verified.

![Log In](documentation/myaccount-list-image.png)

## Wishlist:

- Adding and removing products from the wishlist were tested for accurate functionality.
- Success and error messages were validated for wishlist actions.

![Wish List](documentation/wishlist-loggedin-image.png)

## Shopping Bag:

- Adding products to the shopping bag and updating quantities were tested.
- Checkout process was tested for accuracy, including order summary display and order placement.

![Shopping Bag](documentation/carticon-image.png)

![Shopping Bag Page](documentation/cart-image.png)


## Product Management:

- Adding, editing, and deleting products and product attributes were tested.
- Image upload functionality for products was validated.

## Category and Tag Management:

- Adding, editing, and deleting categories and tags were tested.
- Assigning categories and tags to products were validated.

## Personnel Management:

- Product units management functionalities were tested.
- Personnel access to product and order management pages was verified.

## Error Handling:

- Error messages and validation checks were tested throughout the application.
- Proper error handling and user feedback mechanisms were validated.

## User Experience:

- Overall user experience and interface responsiveness were tested across different devices and screen sizes.
- Application performance and loading times were evaluated for optimal user experience.

The testing process ensured that all features and functionalities of the e-commerce platform operate smoothly and accurately under various user roles and scenarios.

---

## Validation

### HTML Validation:
- I have had errors during testing when passing through the official [W3C](https://validator.w3.org/) validator, but due to lack of time i was not able to fix them.
i'm gonna work on them later on.

- [Home app HTML validation report](documentation/home-validator.png)

- [Products app HTML validation report](documentation/products-validator.png)

- [Bag app HTML validation report](documentation/bag-validator.png)

- [Checkout app HTML validation report](documentation/checkout-validator.png)

- [Wishlist app HTML validation report](documentation/wishlist-validator.png)


### CSS Validation:

- [Full CSS Validation Report](documentation/css-validator.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator except for the warnings about the use of css root variables and webkits for the box-shadow. However, css code works perfectly on various devices.


### JS Validation:

- [Full JS Validation Report](documentation//js-validator.png)

- Three warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator. However, to validate js full `/* jshint esversion: 8, jquery: true, scripturl: true */` was added to the top of the file.


### Python Validation:

- Some errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/).
- The most common error is that the line is too long.


---
## Lighthouse Report

LightHouse is a web performance testing tool that can be used to evaluate the performance of a website. The report is generated by Google Chrome.

[Lighthouse Home](documentation/lighthouse-home.png)
[Lighthouse Products](documentation/lighthouse-products.png)
[Lighthouse Bag](documentation/lighthouse-bag.png)

---

## Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

---

## Deployment and Payment setup


## Deployment Steps

1. **Sign up for Heroku**: If you haven't already, sign up for a Heroku account at [https://www.heroku.com/](https://www.heroku.com/) and log in.

2. **Install Heroku CLI (Command Line Interface)**: Download and install the Heroku CLI appropriate for your operating system. You can find installation instructions [here](https://devcenter.heroku.com/articles/heroku-cli).

3. **Prepare your app**: Ensure that your app is ready for deployment. This includes making sure all necessary dependencies are listed in your `requirements.txt` or `package.json` file, and any configuration settings are properly set.

4. **Initialize Git repository**: If you haven't already, initialize a Git repository in your project directory.

    ```
    git init
    ```

5. **Login to Heroku**: In your terminal or command prompt, log in to your Heroku account using the Heroku CLI.

    ```
    heroku login
    ```

6. **Create a new Heroku app**: Use the Heroku CLI to create a new app.

    ```
    heroku create
    ```

7. **Deploy your app**: Deploy your app to Heroku using Git.

    ```
    git add .
    git commit -m "Initial deployment"
    git push heroku master
    ```

8. **Open your app**: Once the deployment is complete, you can open your app using the following command:

    ```
    heroku open
    ```

9. **View logs**: You can view logs of your app to debug any issues that may arise during deployment or while your app is running.

    ```
    heroku logs --tail
    ```

These steps should give you a good starting point for deploying your app to Heroku. Make sure to adapt them to your specific app and requirements.


## Database Deployment Steps

1. **Sign up for ElephantSQL**: If you haven't already, sign up for an ElephantSQL account at [https://www.elephantsql.com/](https://www.elephantsql.com/) and log in.

2. **Create a new database instance**: After logging in, navigate to your ElephantSQL dashboard and click on the "Create New Instance" button.

3. **Select a plan**: Choose a plan that suits your needs. ElephantSQL offers various plans with different features and pricing options.

4. **Configure your database**: Specify the configuration details for your database instance, including the region, database version, and instance size.

5. **Provide authentication credentials**: Set up a username and password for accessing your database. Make sure to choose a strong password for security purposes.

6. **Deploy your database**: Once you have configured the necessary settings, click on the "Create" or "Deploy" button to create and deploy your database instance.

7. **Access your database**: After the deployment is complete, you will be provided with connection details such as the host, port, database name, username, and password. Make note of these details as you will need them to connect to your database from your application.

8. **Connect your application to the database**: Update your application's database configuration settings to use the connection details provided by ElephantSQL. This typically involves updating your application's database URL or connection string.

9. **Test the connection**: Verify that your application can successfully connect to the deployed database instance. You can do this by running your application locally or through any testing environment you have set up.

10. **Monitor and manage your database**: Use the monitoring and management tools provided by ElephantSQL to keep track of your database's performance, monitor usage metrics, and perform administrative tasks such as backups and restores.

These steps should guide you through the process of deploying your database to ElephantSQL and integrating it with your application.

## Payment Setup using Stripe

1. **Sign up for a Stripe account**: If you haven't already, sign up for a Stripe account at [https://stripe.com/](https://stripe.com/) and log in.

2. **Navigate to the Dashboard**: Once logged in, you'll be directed to the Stripe Dashboard. This is where you'll manage your Stripe account and configure your payment settings.

3. **Activate your account**: Before you can start accepting payments, you may need to complete Stripe's verification process. Follow the prompts in the Dashboard to provide any necessary information and activate your account.

4. **Obtain API keys**: In the Dashboard, navigate to the "Developers" section and locate your API keys. You'll need these keys to integrate Stripe with your application. Stripe provides both test and live API keys for development and production environments, respectively.

5. **Integrate Stripe SDK**: Depending on your programming language and framework, integrate the Stripe SDK into your application. Stripe provides official SDKs for various languages and platforms, including JavaScript, Python, Ruby, PHP, and more. Follow the installation and setup instructions provided in the Stripe documentation for your chosen SDK.

6. **Configure payment options**: Determine what payment options you want to offer to your users, such as credit/debit cards, Apple Pay, Google Pay, etc. Configure these options in the Dashboard under the "Payments" or "Settings" section.

7. **Implement checkout process**: Design and implement the checkout process in your application. This typically involves creating a form where users can enter their payment information and submitting it to your server.

8. **Tokenize payment details**: Use the Stripe SDK to tokenize the payment details entered by the user. This process securely converts sensitive card information into a unique token that you can safely send to your server for processing.

9. **Process payments on your server**: Receive the tokenized payment details on your server and use the Stripe SDK to initiate payment processing. This involves creating a charge or payment intent using the token and your Stripe API keys.

10. **Handle payment confirmation**: Once the payment is processed successfully, handle the confirmation response from Stripe. Update your application's database or user interface accordingly to reflect the completed payment.

11. **Test payments**: Before launching your application, thoroughly test the payment functionality using Stripe's test environment and test card numbers. Ensure that payments are processed correctly and that error handling is in place for any potential issues.

12. **Go live**: Once you're confident that everything is working as expected, switch to live mode in the Stripe Dashboard and replace your test API keys with your live API keys. Your application is now ready to accept real payments from users.

These steps should guide you through the process of setting up payment using Stripe in your application. Refer to the Stripe documentation and guides for detailed information on specific integration steps and best practices.


- The app can be reached by the [link](https://honeyshop-58be54febc57.herokuapp.com/).
---

