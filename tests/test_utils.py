from makeup.utils import Store

class TestStore:
    s = Store(test_get='success')

    def test_store_set(self):
        self.s.new_data = 123
        assert self.s.new_data == 123

    def test_store_get(self):
        assert self.s.test_get == 'success'

    def test_store_update(self):
        self.s.foo = 'bar'
        assert self.s.foo == 'bar'
        self.s.foo = 'baz'
        assert self.s.foo == 'baz'

    def test_store_set_dict(self):
        self.s['New Data'] = 123
        assert self.s['New Data'] == 123
    
    def test_store_get_dict(self):
        assert self.s['test_get'] == 'success'
