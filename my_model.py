import pickle
import numpy as np
class My_model:
  def __init__(self):
    self.model = pickle.load(open('model.pkl','rb'))

  def predict(self, data):
    self.prepared_data = self.prepare_data(data)
    print(self.prepared_data)
    print(self.prepared_data.shape)
    return self.model.predict(self.prepared_data)[0]

  def prepare_data(self, data):
    from sentence_transformers import SentenceTransformer
    #model_encod = SentenceTransformer('bert-base-multilingual-cased')
    #pickle.dump(model_encod, open('model_encod.pkl','wb'))
    model_encod = pickle.load(open('model_encod.pkl', 'rb'))
    x, y = data['book_desc'], data['book_genre']
    t = (data['book_rating_count'] -33723.66)/198754.65
    data1 = np.array(list(model_encod.encode(x)) + list(model_encod.encode(y)) + [t])
    return data1.reshape(1, -1)
