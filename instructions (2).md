# Flask EX2

**Directions**: In this exercise, you will complete the flask project. There is quite a bit of starter code, and
understanding how the starter code works will set you up for success on this exercise.

**IMPORTANT**: Before you take the starter code from Schoology, make sure you have completed Part 1.

## [Example Final Product](https://drive.google.com/file/d/11xvwY2GcQB7aGa7fHkx_DjNX7nRbLuq1/view?usp=sharing)

**Requirements**: After watching Part 2, please do the following:

1. Create a new route that handles the /delete_product action from the delete button on the homepage. This route should
   successfully delete a product the database and redirect back to index while keeping the same category of products
   open.
2. Create a new route that handles the /category_list that runs when the List Categories link is clicked. This route
   should render the *category_list.html* document.
3. You will need to add the HTML to *category_list.html* to complete the table with all category names on the left
   column and delete buttons on the right column. There also needs to be an HTML form at the bottom that takes a single
   text input and an Add Category button. This will allow the user to add a category to the database.
4. Create a new route to handle the /add_category action from the form you created. The action should read from the POST
   array and add the category input to the database.
5. Create a new route to handle the /delete_category action that occurs when a delete button is clicked. This route
   should successfully delete a category **if and only if the category has no products**. If there are products in the
   category, render the *error.html* page and set the error variable to something relevant.

### Extra Credit (3 Points)

Create another model file that contains functions that will validate the data. Use these functions to send custom
messages to the *error.html* page using the error variable. Make sure to cover all possible ways data could come in as!

### Extra Extra Credit (3 Points)

Create a *tests* folder in model folder. Inside of this folder write Python unittests to fully test your model. Make
sure to fully test each function that is used in the model.