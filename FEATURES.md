# Features

## Access to pages according to the user role:

| Page Name                      | Logged out | Customers | Manager | Admin                 |
| ------------------------------ | ---------- | --------- | ------- | --------------------- |
| Home                           | Yes        | Yes       | Yes     | Yes                   |
| Login                          | Yes        | Yes       | Yes     | Yes                   |
| Register                       | Yes        | Yes       | Yes     | Yes                   |
| Logout                         | Yes        | Yes       | Yes     | Yes                   |
| Store Products                 | Yes        | Yes       | Yes     | Yes                   |
| Store Product's Details        | Yes        | Yes       | Yes     | Yes                   |
| All reviews                    | Yes        | Yes       | Yes     | Yes                   |
| Bag                            | No         | Yes       | Yes     | Yes                   |
| My Orders                      | No         | Yes       | Yes     | Yes                   |
| My Order's Details             | No         | Yes       | Yes     | Yes                   |
| My Wishlist                    | No         | Yes       | Yes     | Yes                   |
| Checkout                       | No         | Yes       | Yes     | Yes                   |
| Create newsletter              | No         | No        | Yes     | Yes                   |
| Categories                     | No         | No        | Yes     | Yes                   |
| Add category                   | No         | No        | Yes     | Yes                   |
| Edit category                  | No         | No        | Yes     | Yes                   |
| Delete category                | No         | No        | No      | Yes                   |
| Tags                           | No         | No        | Yes     | Yes                   |
| Add tag                        | No         | No        | Yes     | Yes                   |
| Edit tag                       | No         | No        | Yes     | Yes                   |
| Delete tag                     | No         | No        | Yes     | Yes                   |
| Products' Types                | No         | No        | Yes     | Yes                   |
| Add product's type             | No         | No        | Yes     | Yes                   |
| Edit product's type            | No         | No        | Yes     | Yes                   |
| Delete product's type          | No         | No        | No      | Yes                   |
| Products' attributes           | No         | No        | Yes     | Yes                   |
| Add product's attribute        | No         | No        | Yes     | Yes                   |
| Edit product's attribute       | No         | No        | Yes     | Yes                   |
| Delete product's attribute     | No         | No        | No      | Yes                   |
| Product's values               | No         | No        | Yes     | Yes                   |
| Add product's value            | No         | No        | Yes     | Yes                   |
| Edit product's value           | No         | No        | Yes     | Yes                   |
| Delete product's value         | No         | No        | No      | Yes                   |
| Personnel Products Table       | No         | No        | Yes     | Yes                   |
| Add product                    | No         | No        | Yes     | Yes                   |
| Edit product                   | No         | No        | Yes     | Yes                   |
| Delete product                 | No         | No        | Yes     | Yes                   |
| Add new image modal            | No         | No        | Yes     | Yes                   |
| Edit image modal               | No         | No        | Yes     | Yes                   |
| Delete image modal             | No         | No        | Yes     | Yes                   |
| Add product's unit             | No         | No        | Yes     | Yes                   |
| Edit product's unit            | No         | No        | Yes     | Yes                   |
| Delete product's unit          | No         | No        | Yes     | Yes                   |
| Product's units                | No         | No        | Yes     | Yes                   |
| Product's unit's details       | No         | No        | Yes     | Yes                   |
| Orders                         | No         | No        | Yes     | Yes                   |
| Order's details                | No         | No        | Yes     | Yes                   |
| Edit order status feature      | No         | No        | No      | Yes + Logistics manager   |
| Edit Order                     | No         | No        | No      | Yes                   |
| Delete order                   | No         | No        | No      | Yes                   |
| Edit order's item              | No         | No        | No      | Yes                   |
| Delete order's item            | No         | No        | No      | Yes                   |


## Main Features:

- Each page has a navbar and a footer beside account's pages.

### Navbar:

- The Navbar has:
    - logo, which redirects to the home page;

    ![Logo](documentation/logo-image.png)

    - All products, a list appears to arrange the display of products on the site according to what the user chooses;
    ![All Products List](documentation/all-products-list-image.png)
    ![All Products](documentation/all-products-image.png)

    - Raw honey, which redirects to the raw honey page;
    
    ![Raw Honey](documentation/rawhoney-image.png)
    ![Raw Honey Products](documentation/rawhoney-products-image.png)

    - Pure honey, which redirects to the pure honey page;

    ![Pure Honey](documentation/purehoney-image.png)
    ![Pure Honey Products](documentation/purehoney-products-image.png)

    - Special Offers honey, which redirects to the special offers page;

    ![Special Offers](documentation/specialoffers-image.png)
    ![Special Offers Products](documentation/specialoffers-products-image.png)

    - Products, raw honey, pure honey, special offers pages, have sort selector;
    ![Sort Selector](documentation/sort-selector-image.png)

    - Wish List, which redirects to the wish list page;

    ![Special Offers](documentation/wishlist-image.png)
    - If the user not logged in it will redirects him to sign in page;
    ![Sign In](documentation/signin-image.png)
    - If the user is already logged in it will redirects him to wishlist page;
    ![Wish List](documentation/wishlist-loggedin-image.png)

    - My Account, which redirects to the register or log in page;

    ![My Account](documentation/myaccount-image.png)
    ![Register/Log In](documentation/myaccount-list-image.png)

    - Shopping Bag, which redirects to the shopping bag;

    ![Shopping Bag](documentation/carticon-image.png)
    ![Shopping Bag Page](documentation/cart-image.png)

    - Search Field, let the user search for specific products;

    ![Shopping Bag](documentation/searchfield-image.png)

### Home page:

![Home page](documentation/main-image.png)

Home page has:

- Delivery Banner:

  ![Delivery Banner](documentation/delivery-banner-image.png)

- Hero Section:

  ![Hero Section](documentation/hero-section-image.png)

- Shop Now Button, which redirects to the products page:

  ![Shop Now Button](documentation/shop-now-button.png)
  ![Shop Now Products](documentation/shop-now-products.png)

### Footer:

![Footer](documentation/footer-image.png)

Footer has the following features:

- Newletter Subscription, which redirects to the newsletter page;

![Newsletter](documentation/newsletter-image.png)

- After submitting the newsletter subscription, the user will be directed to success page;

![Success](documentation/success-image.png)

- If the user already subscribed, a message will shows up for the user;

![Subsciber Exists](documentation/subscriber-exists-image.png)


### Sign Up steps:

![Sign Up](documentation/signup-form-image.png)

- After the user filling the form and clicking sign-up button, an email verification message will shows up;

![verification](documentation/verification-image.png)

- The user then need to login to his email, and confirm his email address using the url that has been sent to him;

![Email Confirm](documentation/email-confirm-image.png)

- At the same time an alert message will shows up on the home page;

![Confirm Alert](documentation/confirm-alert-image.png)

- After clicking the url a confirm email address page will show up;

![Confirm Page](documentation/email-confirm-page-image.png)

- After clicking the confirm button, the user will be redirected to the home page with success message ;

![Confirm Success](documentation/confirm-success-message-image.png)

- Now the user need to click on my account icon and then click on login;

![Log In](documentation/myaccount-list-image.png)

- If the user forgot his password, he can click on (Forgot your password?) link, it will redirect the user to reset password page;

![Reset Password](documentation/reset-password-image.png)

- After the user input his email address and reset my password button, a message will shows up for the user confirming that a link has been sent to his email address;

![Reset Password Link](documentation/reset-password-link-image.png)

- Now after clicking on the link in the email message, the user will be redirected to change password page;

![Change Password](documentation/change-password-image.png)

- After changing the password, a success page will shows up;

![Success Page](documentation/change-password-success-image.png)

- When the user click on back to home page button, he will be redirected to the home page with success message;

![Home Success](documentation/change-password-success-home-image.png)


### wishlist:

![Wish List](documentation/add-to-wishlist-image.png)

- To add a product to wishlist, the user should be logged in;

- After adding a product to wishlist, a success message will shows up;

![Wishlist Success](documentation/wishlist-success-image.png)

- To remove a product from the wishlist, user need to click on remove button;

![Wishlist Remove](documentation/wishlist-remove-image.png)

### Bag: