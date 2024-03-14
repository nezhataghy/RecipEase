const displayBuffer = function() {
    $('.menu-meal').remove();
    $('.section-menu .container').prepend(`
    <div class="buffer fa-3x flex justify-center min-h-96">
        <i class="fa-solid fa-solid fa-utensils fa-fade text-sec-dark"></i>
    </div>
    `)
}

const displayErrorMsg = function(errMsg) {
    $('.section-menu .container').prepend(`
    <div class="error-container flex justify-center">
        <p class="error-msg">${errMsg}</p>
    </div>
    `)
}

$(document).ready(function() {
    const getFood = async function(category) {
        try {
            displayBuffer();
            const response = await fetch(`http://recipease.me/api/food/category/${category}`);
            const food = await response.json();
            if (!food) throw new Error('Failed to fetch, Check your internet connection.xx');
            return food;
        } catch (err) {
            displayErrorMsg(err.message);
        } finally {
            $('.buffer').remove();
            $('.error-container').remove();
        }
    }

    const displayDefaultMenu = async function () {
        $('.breakfast-btn').addClass('active-menu_btn');
        try {
        const result = await getFood('breakfast');
        if (!result) throw new Error('Failed to fetch, Check your internet connection')
        let food = result.food;
        food = food.slice(0, 10)
        food.forEach(meal => {
            let ingredients = [];
            meal.ingredients.forEach(ing => {
                ingredients.push(ing.name)
            });
            $('.menu').append(`
            <div class="menu-meal">
                <div class="foodname_img flex justify-between items-center relative overflow-hidden mt-4">
                    <h3 class="foodname relative z-10 after:font-thin after:text-main-dark sm:text-base">${meal.name}</h3>
                    <img src="${meal.image}"
                    class="menu-img"
                    data-mealID="${meal.__id}"/>
                </div>
                <p class="food-ingredients text-sec-med font-light">${ingredients.join(', ')}</p>
            </div>
            `)
        })
        } catch (err) {
            displayErrorMsg(err.message);
        }
    }

    displayDefaultMenu()

    const menuFilter = async function(e) {
        // The target should contain class `menu-btn` to continue.
        if (!$(e.target).hasClass('menu-btn')) return;

        // Fetching data filtered by category by clicking the menu buttons.
        const clickedCategory = $(e.target).data('category');
        try {
        const result = await getFood(clickedCategory);
        if (!result) throw new Error("Failed to fetch, Check your internet connection")
        let food = result.food;
        food = food.slice(0, 10)

        // Remove the active button if another button clicked
        Array.from($('.menu-btn')).forEach(btn => {
            if ($(btn).hasClass('active-menu_btn')) $(btn).removeClass('active-menu_btn');
        });

        // Activate the button
        $(e.target).addClass('active-menu_btn')

        // Remove the data already displayed
        // $('.menu-meal').remove();

        // Display the data based on the category that chosen.
        food.forEach(meal => {
            let ingredients = [];
            meal.ingredients.forEach(ing => {
                ingredients.push(ing.name)
            });
            $('.menu').append(`
            <div class="menu-meal">
                <div class="foodname_img flex justify-between items-center relative overflow-hidden mt-4 ">
                <h3 class="foodname relative z-10 after:font-thin after:text-main-dark">${meal.name}</h3>
                <img src="${meal.image}"
                class="menu-img"
                data-mealID="${meal.__id}"/>
                </div>
                <p class="food-ingredients text-sec-med font-light">${ingredients.join(', ')}</p>
            </div>
            `)
        })
        } catch (err){
            displayErrorMsg(err.message);
        }
    }

    $('.options').click(menuFilter)

    const mealLink = function(targetEle) {
        if (!$(targetEle).data('mealid')) return;
    
        const mealClicked = $(targetEle);
        const mealId = mealClicked.data('mealid');
        window.location.href = `meal.html?id=${mealId}`;
    }

    $('.menu').click(function (e) {
        if (!$(e.target).hasClass('menu-img')) return;

        const menuImg = $(e.target);
        mealLink(menuImg)
    })

});
