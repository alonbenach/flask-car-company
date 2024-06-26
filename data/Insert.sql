INSERT INTO Dealers (dealer_name,dealer_address) Values('Joes Autos', '123 Abc Lane Virginia');
INSERT INTO Dealers (dealer_name,dealer_address) Values('Priority X', '999 Nein-Nein Virginia');
INSERT INTO Dealers (dealer_name,dealer_address) Values('Priority Y', '404 Address Not Found');
INSERT INTO Dealers (dealer_name,dealer_address) Values('Priority Z', '8675309 Jessies Mom');
INSERT INTO Brands(brand_name) Values('Cover Squirrel');
INSERT INTO Brands(brand_name) Values('Supreme');
INSERT INTO Brands(brand_name) Values('Yellow');
INSERT INTO Brands(brand_name) Values('Ferrari');
INSERT INTO Brands(brand_name) Values('Boujiee');
INSERT INTO Brands(brand_name) Values('Freshest');
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(1,1);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(1,3);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(1,6);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(1,5);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(2,2);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(2,3);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(2,5);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(2,1);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(3,5);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(3,6);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(3,2);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(4,2);
INSERT INTO Dealer_Brand(dealer_id, brand_id) Values(4,4);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("The Blonde", 23000, 1);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("The Brunette", 25000, 1);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("The Red Head", 29000, 1);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Hat", 22000, 2);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Sweater", 25000, 2);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("T-Shirt", 27000, 2);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Orange", 15000, 3);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Blue", 12000, 3);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Green", 17000, 3);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("LaFerrari", 125000, 4);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("450", 75000, 4);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("F12 Berlinetta", 110000, 4);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("F40", 100000, 4);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Extra", 30000, 5);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Too Much", 35000, 5);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Beats", 24000, 6);
INSERT INTO Models(model_name, model_base_price, brand_id) Values("Bars", 35000, 6);
INSERT INTO Manufacture_Plant(plant_name, plant_type, plant_location, company_owned) Values("West Plant", "Parts", "Europe",1);
INSERT INTO Manufacture_Plant(plant_name, plant_type, plant_location, company_owned) Values("East Plant", "Parts", "Asia",1);
INSERT INTO Manufacture_Plant(plant_name, plant_type, plant_location, company_owned) Values("North Plant", "Assembly", "Asia",1);
INSERT INTO Manufacture_Plant(plant_name, plant_type, plant_location, company_owned) Values("South Plant", "Assembly", "Australia",1);
INSERT INTO Manufacture_Plant(plant_name, plant_type, plant_location, company_owned) Values("Scranton Branch", "Parts", "USA",0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date) Values ('2.6L Engine', 1, '2012-08-12', '2013-08-12');
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('3.0L Engine', 2, '2012-07-10', '2017-02-20', 0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('2.4L Engine', 5, '2012-08-12', '2013-08-12', 0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('Jetrag 6 Speed', 5, '2012-02-11', '2013-08-12', 0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('Bose Audio', 1, '2014-08-02', '2015-03-12', 0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('4WD Chassis', 2, '2000-08-29', '2017-05-12', 0);
INSERT INTO Car_Parts(part_name, manufacture_plant_id, manufacture_start_date, manufacture_end_date, part_recall) Values ('2WD Chassis', 2, '2005-12-20', '2017-11-01', 0);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(4,2,4,6,5,"Blue",2000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(5,2,4,6,5,"Yellow",1200);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(6,1,4,7,5,"Green",1100);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(15,1,4,7,5,"Red",4000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(14,2,4,7,5,"Sky",3000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(16,2,4,7,5,"Birthday Cake",2500);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(17,3,4,6,5,"Cyan",7000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(10,1,4,6,5,"Purple",2500);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(11,2,4,6,5,"Red",10000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(12,2,4,7,5,"Blue",11300);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, premium_sound_id, color, option_set_price) Values(13,1,4,7,5,"Green",23000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(1,1,4,7,"Black",1100);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(2,1,4,7,"Blue",2000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(3,1,4,6,"Red",1500);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(4,3,4,6,"Yellow",4000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(5,2,4,6,"Black",3600);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(7,2,4,6,"White",2300);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(8,2,4,7,"Pretty",2200);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(9,3,4,7,"Glitter BomB",2900);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(14,1,4,7,"Nyan",7999);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(12,1,4,7,"Ultraviolet",25000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(11,1,4,7,"Transparent",40000);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(6,2,4,6,"Green",1200);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(2,1,4,6,"Purple",3900);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(1,2,4,7,"Red",900);
INSERT INTO Car_Options(model_id, engine_id, transmission_id, chassis_id, color, option_set_price) Values(11,2,4,6,"Magenta",200);
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Jeremy","Jacobs","Male",120000,"1990-12-12",9177554315,"Jeremy@Gmail.com");
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Maria","Swabota","Female",60000,"1980-06-15",7577749387,"Maria@Gmail.com");
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Jacob","Wong","Male",24000,"1992-02-20",2129990234,"WonTon@hotmail.com");
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Pitbull","Perez","Male",1200000,"1985-12-01",7892341827,"Pitbull@ymail.com");
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Minnie","Mouse","Female",200000,"1950-03-01",7542890987,"MinnieMe@gmail.com");
INSERT INTO Customers(first_name, last_name, gender, household_income, birthdate, phone_number, email) Values("Jessica","Parker","Female",120000,"1989-06-29",4245679000,"JennyFromThePark@mymail.com");
INSERT INTO Car_Vins(vin, model_id, option_set_id, manufactured_date, manufactured_plant_id) Values(6480649, 7,17,"2017-02-20",4);
INSERT INTO Car_Vins(vin, model_id, option_set_id, manufactured_date, manufactured_plant_id) Values(3000587, 14,5,"2016-09-19",3);
INSERT INTO Car_Vins(vin, model_id, option_set_id, manufactured_date, manufactured_plant_id) Values(3358900, 12,10,"2014-11-14",3);
INSERT INTO Car_Vins(vin, model_id, option_set_id, manufactured_date, manufactured_plant_id) Values(9975348, 2,13,"2013-03-04",4);
INSERT INTO Car_Vins(vin, model_id, option_set_id, manufactured_date, manufactured_plant_id) Values(3434978, 4,1,"2013-06-22",4);
INSERT INTO Customer_Ownership(customer_id, vin, purchase_date, purchase_price, warranty_expire_date, dealer_id) Values(6,6480649,"2017-12-21",17200,"2025-05-12",2);
INSERT INTO Customer_Ownership(customer_id, vin, purchase_date, purchase_price, warranty_expire_date, dealer_id) Values(5,3000587,"2016-10-14",33000,"2024-04-19",1);
INSERT INTO Customer_Ownership(customer_id, vin, purchase_date, purchase_price, warranty_expire_date, dealer_id) Values(2,3358900,"2015-12-01",121300,"2026-03-03",4);
INSERT INTO Customer_Ownership(customer_id, vin, purchase_date, purchase_price, warranty_expire_date, dealer_id) Values(3,9975348,"2017-08-09",26000,"2090-02-14",1);
INSERT INTO Customer_Ownership(customer_id, vin, purchase_date, purchase_price, warranty_expire_date, dealer_id) Values(1,3434978,"2017-02-24",24000,"2027-01-12",3);
