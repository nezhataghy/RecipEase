const urlParams = new URLSearchParams(window.location.search);
const paramId = urlParams.get('id');

$(document).ready(function() {
    const getMeal = function() {
        $.get(`http://recipease.me/api/food/${paramId}`, function (data, status){  
            if (status == 'success') {
                const meal = data.meal;
               
                $('.meal-image').css('background-image', `url("${meal.image}")`);

                $('.details').append(`
                <div class="meal-details">
                        <h2 class="meal-name mt-3 mb-6 font-bold text-sec-dark text-2xl text-center">${meal.name}</h2>
                        <div class="grid md:grid-cols-3 sm:gap-y-4">
                            <ul class="meal-recipe md:col-span-2 bg-sec-extralight shadow-md p-3 md:w-11/12">
                                <h2 class="mb-4 font-extrabold text-main-dark md:text-xl md:text-left text-center">Recipe</h2>
                            </ul>

                            <ul class="meal-ingredients md:col-span-1 bg-sec-extralight shadow-md p-3">
                                <h2 class="mb-4 font-extrabold text-main-dark md:text-xl md:text-left text-center">Ingredients</h2>
                            </ul>
                        </div>
                    </div>
                `)
                
                if (!meal.recipe) return;

                const mealRecipe = meal.recipe.content.split('__');
                if (!mealRecipe) return;

                // Display food recipe
                mealRecipe.forEach((bullet, i) => {
                    $('.meal-recipe').append(`
                    <div class="recipe-bullet flex items-start mt-3">
                        <span class="font-bold text-sec-med text-2xl">${i + 1}.</span>
                        <li class="mb-3 mt-1 pl-2.5 w-4/5">${bullet}</li>
                    </div>
                    `)
                });

                // Display food ingredients
                meal.ingredients.forEach((ingredient, i) => {
                    $('.meal-ingredients').append(`
                    <div class="recipe-bullet flex items-start mt-3">
                        <span class="font-bold text-sec-med text-2xl">${i + 1}.</span>
                        <li class="mb-3 mt-1 pl-2.5">${ingredient.name}</li>
                    </div>
                    `)
                });


                /*
                <div class="recipe-bullet flex items-start mt-3">
                    <span class="font-bold text-sec-med text-2xl">01.</span>
                    <li class="mb-3 mt-1 pl-2.5">1. Lorem</li>
                </div>
                
                */
            }
        });
    }
    getMeal()
});
