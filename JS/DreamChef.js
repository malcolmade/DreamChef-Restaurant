
/*
    html onClick():
        nav main:
            sign in
            basket
            btn change address
            link address

        footer:
            order

*/
/*
    JS eventhandler():
        nav main:
            btn order now
        nav sub:
            btn order for collection
            btn order for delivery

        showcase favs:
            btn_fav01 to (btn_fav05)

*/


/* let menu-group = {id:"", name:"", info:"", countMax:5, price:0.00} */

// To be loaded from PYTHON
//const xmenu_set = ["Salads", "Chicken", "Beef", "Lamb", "Pork", "Rice", "Pasta", "Quinoa", "Sides", "Deserts", "Drinks", "Deals"]

// menu-groups
const menuGroup_id = ("A10021", "B33001", "C75401", "D82701", "E27301", "F53933", "G12101", "H40093", "I66603", "J00666", "K99903", "L30999");
const menuGroup_name = ("Salads", "Chicken", "Beef", "Lamb", "Pork", "Rice", "Pasta", "Quinoa", "Sides", "Deserts", "Drinks", "Deals")
const menuGroup_info = ("Great Tasting", "Awesome Aroma", "Tender as can be", "Flavour from around the globe", "Very addictive", "Finger licking good", "Crispy and succulent", "Straight from the meditarranean", "Ideal meal partners", "Endulge yourself", "Quench your thirst", "Combination of perfect tastes");
const count_menuGroupSub = [4, 3, 2, 1, 3, 1, 3, 2, 2, 3, 3, 4];
//

//
const menuGroup_subItem = new Array(count_menuGroupSub[0]);
menuGroup_subItem[0] = {id:"Aa021", name:"Aragula Salad", info:"Best in Town1", count:5, price:11.45};
menuGroup_subItem[1] = {id:"Ab021", name:"Caprese Salad", info:"Best in Town2", count:5, price:5.95};
menuGroup_subItem[2] = {id:"Ac021", name:"Tabbouleh Salad", info:"Best in Town3", count:5, price:9.99};
menuGroup_subItem[3] = {id:"Ad021", name:"Tuna Salad", info:"Best in Town4", count:5, price:14.95};
//
//const menuGroup_sub = new Array(count_menuGroupSub[0]);
const menuGroup_sub = [menuGroup_subItem[0], menuGroup_subItem[1], menuGroup_subItem[2], menuGroup_subItem[3]];



// ------------------------------------------------------------------------------------------------------------

// let cur_pg = 'home'

const count_menuGroup = 12;
const menu_group = new Array(count_menuGroup);
//
menu_group[0] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
                items: {}};
//
menu_group[1] = {id:"1", name:"CHICKEN", info:"Awesome crunchy tastiest chicken",
                items: {}};
//
menu_group[2] = {id:"1", name:"BEEF", info:"Our beef has been cured for days and marinated with flavours to crave for",
items: {}};
//
menu_group[3] = {id:"1", name:"LAMB", info:"Specily prepared rare lamb that has been cured for days and marinated with flavours to crave for",
items: {}};
//
menu_group[4] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
items: {}};
//
menu_group[5] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
items: {}};

menu_group[6] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
 items: {}};
 
menu_group[7] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
items: {}};

menu_group[8] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
 items: {}};
 
menu_group[9] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
items: {}};

menu_group[10] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
 items: {}};
 
menu_group[11] = {id:"1", name:"SALADS", info:"Cool autumn days call for hearty, crisp salads with plenty of flavour.\nThat’s all the reason you need to get into our organic Seasonal Salad & Veg. With a mix of multiple different salad and veggie portions, you’ll have all you need to lay on a luscious salad spread.",
items: {}};


// 
let user = {name_first: '', name_last: '', tel: '', dob: null, pwd: '', e_mail: '', adr: '', adr_bill: '', adr_delv: '', comms:{e_mail: false, sms: false}, pol_agree: false, signed_in: false}
//
let order = {type: '', id: '', name: '', items: {name: '', price: 0.0, count: 0, sub_tot: 0.0}}



console.log("tester = " + menu_group[0].sub[3].price);
console.log("tester = " + menu_group[0].sub[1].name);


/*
// menu-items
const menuItem_id = new Array(countMax_menuGroup);
menuItem_id[0] = ("Aa021", "Ab021", "Ac021", "Ad021");
menuItem_id[1] = ("Ba001", "Bb001", "Bc001", "Bd001");
menuItem_id[2] = ("Ca401", "Cb401", "Cc401", "Cd401");
menuItem_id[3] = ("Da701", "Db701", "Dc701", "Dd701");
menuItem_id[4] = ("E27301", );
menuItem_id[5] = ("F53933", );
menuItem_id[6] = ("G12101", );
menuItem_id[7] = ("H40093", );
menuItem_id[8] = ("I66603", );
menuItem_id[9] = ("J00666", "K99903", "L30999");
menuItem_id[10] = ("K99903", "L30999");
menuItem_id[11] = ("L30999");



const menu_prices = ();

//
const menu_set = [];

for (let i = 0; i < countMax_menuSet; i++) {
    menu_set[i] = 
  }


let menu = {id:"", name:"", info:"", countMax:5, price:0.00}

const client_basket = {id:"", subTotal:0.0, payWay:"", adr_deliver:"", items:};
const ordered = {id:"", total:29.98, payWay:"", dt_tm:"", adr_deliver:"123 street"};

let client_signIn = false;
let client = {id:"", name_first:"", name_last:"", dob:"08-09-1990", tel:07730477300, email:"ade@gmail.com", pwd:"", adr_bill:"124 road", adr_deliver:"123 road", ordered_count:4}

const btn_oder = document.getElementById("order_btn");


//
function StateChange_SignIn (){
}

//
function StateChange_OrderType (){
}

/*


/*
const btn_test = document.getElementById("btn_order");
const btn_test2 = document.getElementById("btn_tester");
const dNav = document.getElementById("nav");

btn_test.addEventListener("click", ()=>{
    document.getElementById("disable_div").style.visibility = 'visible';
})


btn_test2.addEventListener("click", ()=>{
   document.getElementById("disable_div").style.visibility = 'hidden';
})
*/