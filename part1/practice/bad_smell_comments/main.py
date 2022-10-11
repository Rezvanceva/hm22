

class Unit:

    def move(self, field, x, y, vector, flay, crawl, point=1):

        if flay and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if flay:
            point *= 1.2
            if vector == 'UP':
                new_y = y + point
                new_x = x
            elif vector == 'DOWN':
                new_y = y - point
                new_x = x
            elif vector == 'LEFT':
                new_y = y
                new_x = x - point
            elif vector == 'RIGHT':
                new_y = y
                new_x = x + point
        if crawl:
            point *= 0.5
            if vector == 'UP':
                new_y = y + point
                new_x = x
            elif vector == 'DOWN':
                new_y = y - point
                new_x = x
            elif vector == 'LEFT':
                new_y = y
                new_x = x - point
            elif vector == 'RIGHT':
                new_y = y
                new_x = x + point

            field.set_unit(x=new_x, y=new_y, unit=self)


