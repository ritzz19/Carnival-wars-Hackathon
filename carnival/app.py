from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Pickle_RFR_Model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Stall_no=float(request.form['Stall_no'])
        Market_Category=int(request.form['Market_Category'])
        Discount_avail = float(request.form['Discount_avail'])
        Charges_1=request.form['Charges_1']
        Minimum_price = request.form['Minimum_price']
        Maximum_price = request.form['Maximum_price']
        Grade= request.form['Grade']
        if(Grade==0):
            Grade=0
        elif(Grade==1):
            Grade =1
        elif (Grade==2):
            Grade = 2
        elif (Grade==3):
            Grade = 3
        Product_Category = request.form['option']
        Product_Category_Child_care = 0
        Product_Category_Cosmetics = 0
        Product_Category_Educational = 0
        Product_Category_Fashion = 0
        Product_Category_Home_Decor = 0
        Product_Category_Hospitality = 0
        Product_Category_Organic = 0
        Product_Category_Pet_Care = 0
        Product_Category_Repair = 0
        Product_Category_Technology = 0

        if (Product_Category== 0):
            Product_Category_Child_care = 1
        elif (Product_Category== 1):
            Product_Category_Cosmetics = 1
        elif (Product_Category== 2):
            Product_Category_Educational = 1
        elif (Product_Category==3):
            Product_Category_Fashion = 1
        elif (Product_Category== 4):
            Product_Category_Home_Decor = 1
        elif (Product_Category== 5):
            Product_Category_Hospitality = 1
        elif (Product_Category== 6):
            Product_Category_Organic = 1
        elif (Product_Category== 7):
            Product_Category_Pet_Care = 1
        elif (Product_Category== 8):
            Product_Category_Repair = 1
        elif (Product_Category== 9):
            Product_Category_Technology = 1

        prediction=model.predict([[Stall_no,Market_Category,Discount_avail,Charges_1,Minimum_price,Maximum_price,Grade,Product_Category_Technology,Product_Category_Repair,Product_Category_Pet_Care,Product_Category_Hospitality,Product_Category_Organic,Product_Category_Child_care,Product_Category_Cosmetics,Product_Category_Educational,Product_Category_Fashion,Product_Category_Home_Decor,]])
        prediction=prediction[0]

        return render_template('index.html', prediction_selling_price='Selling Price is ${:.2f}'.format(prediction))


if __name__=="__main__":
    #app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)
    #app.run(port=5001, debug=True, use_reloader=True)
    app.run(debug=True)
