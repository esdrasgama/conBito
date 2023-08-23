class Movies():

    def __init__(self, id, title,dutation, released) -> None:
        self.id = id
        self.title = title
        self.dutation = dutation
        self.released = released
        
        def to_JSON(self):
            return {
                "id": self.id,
                "title": self.title,
                "dutation": self.dutation,
                "released": self.released
            }   