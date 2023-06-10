"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    class DecoratedClass(cls):
        instances_created = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            DecoratedClass.instances_created += 1

        @classmethod
        def get_created_instances(cls):
            return cls.instances_created

        @classmethod
        def reset_instances_counter(cls):
            prev_count = cls.instances_created
            cls.instances_created = 0
            return prev_count

    return DecoratedClass


@instances_counter
class User:
    pass


if __name__ == '__main__':
    assert User.get_created_instances() == 0
    user1, user2, user3 = User(), User(), User()
    assert user1.get_created_instances() == 3
    assert user2.reset_instances_counter() == 3
    assert user3.get_created_instances() == 0
