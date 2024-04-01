from flet import * 

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb0gff'
    
    categories_card=Row(
        scroll = 'auto'
    )
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(bgcolor = BG, height = 110, width = 170, padding=15, border_radius = 20,
                      content = Column(
                          controls=[
                              Text('40 Tasks'),
                              Text(category),
                              Container(
                                  width = 160,
                                  height = 5,
                                  bgcolor = 'white12',
                                  border_radius = 20,
                                  padding = padding.only(right=30),
                                  content=Container(
                                      bgcolor=PINK
                                  ),
                              )
                              
                          ]
                      ))
        
        )
    
    first_page_contents = Container(
        content = Column(
            controls = [
                Row(alignment = 'spaceBetween',
                    controls = [
                        Container(
                            content = Icon(icons.MENU)
                            ),
                        Row(
                            controls = [
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                                ]
                            )
                        ]       
                    ),    
            
                Text (value = "What\'s up , Dimroid!"),
                Text (value = 'CATEGORIES'),
                Container(
                    padding = padding.only(top=10, bottom=20),
                    content=categories_card
                )
            ]
        )
        
    )
    
    page_1 = Container()
    page_2 = Row(
        controls = [
            Container(
                width = 400,
                height = 850,
                bgcolor = FG,
                border_radius = 35,
                padding = padding.only(
                    top=50, left=20,
                    right = 20, bottom = 5
                ),
                content=Column(
                    controls = [first_page_contents]
                )
            )
        ]
    )
    
    
    container = Container(
        width=400,
        height = 600,
        bgcolor = BG,
        border_radius = 35
        
    )
    page.add(container)
    
    
app(target=main)