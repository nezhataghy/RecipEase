document.addEventListener('DOMContentLoaded', function () {
    $('.food .container').append(`
        <div class="buffer fa-3x flex justify-center items-center">
            <i class="fa-solid fa-solid fa-utensils fa-fade text-sec-dark"></i>
        </div>
        `)
})

const errorMsgDisplay = function(errMsg) {
    $('.food .container').append(`
    <div class="error-container flex justify-center">
        <p class="error-msg">${errMsg}</p>
    </div>
    `)
}

$(document).ready(function() {
    const displayFood = function(food) {
        $('.food-grid').empty();
        food.forEach(meal => {
            $('.food-grid').append(`
            <figure class="meal bg-white pt-5 pb-3 px-5 rounded-lg shadow-lg"">
                <div class="layer">
                    <a><img src="${meal.image}" alt="landing page" class="meal-img cursor-pointer rounded-lg" data-mealID="${meal.__id}"></a>
                </div>
                <figcaption class="mt-2">
                    <h3 class="meal-name text-main-dark font-bold cursor-pointer text-xl ml-2" data-mealID="${meal.__id}">${meal.name}</h3>
                </figcaption>
            </figure>`);
        });
    }

    const getFood = async function() {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/food');
            if (response) {
                data = await response.json();
                const food = data.food;
                displayFood(food);
            }
        } catch (err) {
            console.log(err);
        } finally {
            $('.buffer').remove()
        }
    }

    getFood()

    $('.food-grid').click(function (e) {
    if (!$(e.target).data('mealid')) return;
    
    const mealClicked = $(e.target);
    const mealId = mealClicked.data('mealid');
    window.location.href = `meal.html?id=${mealId}`;
    })

    const searchFood = async function(meal_substr) {
        $('.error-container').remove();

        $('.food .container .search-container').append(`
        <i class="test fa-solid fa-solid fa-utensils fa-fade text-sec-dark text-2xl mt-4"></i>`);

        try {
            const response = await fetch(`http://127.0.0.1:5000/api/search_food/${meal_substr}`);
            const result = await response.json();
            const food = result.food;
            if (!food) throw new Error('Nothing here!');
            displayFood(food);
        
        } catch (err) {
            $('.food-grid').empty();
            errorMsgDisplay(err.message);
        } finally {
            $('.test').remove();
        }
    }

    $('.search-input').on('input', function () {
        if (this.value === '') {
            getFood();
            return;
        }

        searchFood(this.value.toLowerCase());
    });
});
