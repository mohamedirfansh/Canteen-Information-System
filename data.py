import pickle

'''
Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday = 0,1,2,3,4,5,6

outlet = {'Mac Donald':['assets/mcdonald.png','assets/Macs_Menu.png'],
          'Malay Stall':['assets/malaybbq.png','assets/MBBQ_Menu.png'],
          'Beverages Stall':['assets/drinks.png','assets/Beverages_Menu.png'],
          'KFC':['assets/kfc.png','assets/KFC_Menu.png'],
          'Yong Tau Foo Stall':['assets/ytfoo.png','assets/YTF_Menu.png']
          }

main_database = {'Mac Donald':{'Lunch': {'Title': 'Mac Donald Lunch/Dinner',
                                         'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (1100,2400),
                                                             (Saturday,):(1200,2400),
                                                             (Sunday,):(1200,2200)
                                                            },
                                         'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                                  ('♣ Filet O Fish: $3.95',
                                                   '♣ McChicken: $3.95',
                                                   '♣ Vanilla Cone: $0.80',
                                                   '♣ Chicken Nuggets - 6pc: $4.60\n',),
                                                },
                                         'Hours': 'Opening Hours\nMonday - Sunday : 7am to 12 midnight\n\nAfter Hours\nMonday - Friday: 11am to 12 midnight\nSaturday: 11am to 12 midnight\n\nBreakfast Hours\nMonday - Friday: 7am to 11am\nSaturday: 7am to 12pm\nSunday: 10am to 12pm',
                                         'Queue': 2,
                                         'Location': 'Block N2.1,#01-08, 76 Nanyang Dr\n08 Nanyang Technological University, 637331',
                                         'Review': 'assets/Mac_Review.txt'},
                               
                               'Breakfast':{'Title': 'Mac Donald Breakfast',
                                            'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday,): (700,1100),
                                                                (Saturday,):(700,1200),
                                                                (Sunday,):(1000,1200)
                                                               },
                                            'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                                     ('♣ Big Breakfast: $6.95',
                                                      '♣ Hotcakes: $5.95',
                                                      '♣ Breakfast Wrap Chicken: $4.80',
                                                      '♣ Hotcakes: $4.60\n',),
                                                    },
                                           'Hours': 'Opening Hours\nMonday - Sunday : 7am to 12 midnight\n\nBreakfast Hours\nMonday - Friday: 7am to 11am\nSaturday: 7am to 12pm\nSunday: 10am to 12pm\n\nAfter Hours\nMonday - Friday: 11am to 12 midnight\nSaturday: 11am to 12 midnight',
                                           'Queue': 2,
                                           'Location': 'Block N2.1,#01-08, 76 Nanyang Dr\n08 Nanyang Technological University, 637331',
                                           'Review': 'assets/Mac_Review.txt',}
                               },
                 
                 'Malay Stall':{'Malay Stall':{'Title': 'Malay BBQ Stall',
                                               'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                    (Saturday,): (830,1700)
                                                                   },
                                               'Menu': {
                                                 (Monday,): ['Monday\'s Menu',
                                                             '♣ Mee rebus : $3.60*',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Fried Rice Seafood: $4.60',
                                                             '*special dish'],
                                                (Tuesday,): ['Tuesday\'s Menu',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Mee rebus : $3.60*',
                                                             '♣ Nasi kerabu: $5.60*',
                                                             '♣ Fried Rice Seafood: $4.60',
                                                             '*special dish'],
                                               (Wednesday,):['Wednesday\'s Menu',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Fried Rice Seafood: $4.60'],
                                                (Thursday,):['Thursday\'s Menu',
                                                             '♣ Nasi Briyani: $4.60*',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Fried Rice Seafood: $4.60',
                                                             '*special dish'],
                                                 (Friday,): ['Friday\'s Menu',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Mee rebus : $3.60*',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Fried Rice Seafood: $4.60',
                                                             '♣ Laksa: $4.60*',
                                                             '*special dish'],
                                               (Saturday,): ['Saturday\'s Menu',
                                                             '♣ Mee Soto: $3.95',
                                                             '♣ Nasi Ayam Penyet: $4.60*',
                                                             '♣ Chicken Rice: $3.80',
                                                             '♣ Nasi kerabu: $5.60*',
                                                             '♣ Fried Rice Seafood: $4.60',
                                                             '*special dish'],
                                                    },
                                              'Hours': 'Opening Hours\nMonday - Friday: 8:30am to 9:30pm\nSaturday: 8:30am to 5pm\nSunday: Closed',
                                              'Queue': 3,
                                              'Location': '76 Nanyang Drive, N2.1, #02-03\nNanyang Technological University, 637331',
                                              'Review': 'assets/MBBQ_Review.txt'}
                                },
                 
                'Beverages Stall':{'Beverages Stall':{'Title': 'Beverages Stall',
                                                       'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                           (Saturday,): (830,1700),
                                                                          },
                                                        'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday):
                                                                 ('♣ Coffee: $0.70',
                                                                 '♣ Ice Milo: $1.00',
                                                                 '♣ Canned Drinks: $1.00',
                                                                 '♣ Banana Milkshake: $2.10'),
                                                                 },
                                                        'Hours': 'Opening Hours\nMonday - Friday: 8:30am to 9:30pm\nSaturday: 8:30am to 5pm\nSunday: Closed',
                                                        'Queue': 1,
                                                        'Location': '76 Nanyang Drive, N2.1, #02-03\nNanyang Technological University, 637331',
                                                        'Review': 'assets/drinks_Review.txt'}
                                   },
                                   
                 'KFC':{'Lunch':{ 'Title': 'KFC Lunch/Dinner',
                                  'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (1100,2200),
                                                      (Saturday,Sunday): (1100,2000)
                                                     },
                                  'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                           ('♣ Cheese Fries: $4.70',
                                            '♣ Original Recipe Chicken: $3.55',
                                            '♣ Whipped Potato (Medium): $3.40',
                                            '♣ Zinger: $5.30\n'),
                                          },
                                 'Hours': 'Opening Hours\nMonday - Sunday: 7:30am to 10pm\n\nAfter Hours\nMonday - Sunday: 11am to 10pm \n\nBreakfast Hours\nMonday - Friday: 7:30am to 11am',
                                 'Queue': 2,
                                 'Location':'76 NANYANG DRIVE NTU BLK N2.1\n#01-04, 637331',
                                 'Review': 'assets/KFC_Review.txt',
                                 },
                        'Breakfast':{'Title': 'KFC Breakfast',
                                    'Operating Hours': {
                                        (Monday,Tuesday,Wednesday,Thursday,Friday): (730,1100),
                                        },
                                    'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday):
                                             ('♣ Original Recipe Platter: $6.30',
                                              '♣ Original Recipe Porridge: $3.50',
                                              '♣ Original Recipe Twister: $4.50',
                                              '♣ Riser Burger: $4.10\n'),
                                             },
                                    'Hours': 'Opening Hours\nMonday - Sunday: 7:30am to 10pm\n\nBreakfast Hours\nMonday - Friday: 7:30am to 11am \nSaturday - Sunday: No Breakfast\n\nAfter Hours\nMonday - Sunday: 11am to 10pm ',
                                    'Queue': 2,
                                    'Location':'76 NANYANG DRIVE NTU BLK N2.1\n#01-04, 637331',
                                    'Review': 'assets/KFC_Review.txt'}
                                     },
                'Yong Tau Foo Stall':{'Yong Tau Foo Stall':{ 'Title': 'Yong Tau Foo Stall',
                                                            'Operating Hours': {
                                                                (Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                (Saturday,): (830,1700),
                                                                },
                                                            'Menu': {
                                                                (Monday,): ['Monday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60',
                                                                            '♣ Bak Chor Mee: $3.80*',
                                                                            '*special dish'],
                                                                
                                                                (Tuesday,): ['Tuesday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60',
                                                                            '♣ Fried Yee Mee: $5.80*',
                                                                            '♣ Bak Chor Mee: $3.80*',
                                                                            '*special dish'],
                                                                
                                                                (Wednesday,):['Wednesday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60',
                                                                            '♣ Mamak Mee: $4.80*',
                                                                            '*special dish'],
                                                                
                                                                (Thursday,): ['Thursday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60',
                                                                            '♣ Cheong Fun: $4.50*',
                                                                            '*special dish'],
                                                                
                                                                (Friday,): ['Friday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60',
                                                                            '♣ Fish Ball Noodle: $6.30*',
                                                                            '*special dish'],
                                                                
                                                                (Saturday,):['Saturday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: $3.80',
                                                                            '♣ Noodle or Rice: $0.50',
                                                                            '♣ Spicy Soup Base: $0.60'],
                                                                     },
                                                            'Hours': 'Opening Hours\nMonday to Friday: 8:30am to 9:30pm \nSaturday: 8:30am to 5pm \nSunday: Closed',
                                                            'Queue': 3,
                                                            'Location': '76 Nanyang Drive, N2.1, #02-03\nNanyang Technological University, 637331',
                                                            'Review': 'assets/YTF_Review.txt',}
                                     },
                }

#---Pickle dump method to store our database---------
with open("Data.txt",'wb') as file:
    pickle.dump(outlet,file)
    pickle.dump(main_database,file)
'''

#---Pickle load method to read the database that will be used in main.py---------
with open("Data.txt",'rb') as file:
    outlet = pickle.load(file)
    main_database = pickle.load(file)

