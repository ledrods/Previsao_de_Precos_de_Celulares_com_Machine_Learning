import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("C:/projeto1/analise_exploratoria/data/celular2025_clean.csv")

df['Company Name'] = LabelEncoder().fit_transform(df['Company Name'])

# Selecionando as colunas relevantes
X = df[['Company Name', 'RAM', 'Internal Memory', 'Camera Resolution (MP)', 'Battery Capacity (mAh)']]
y = df['avg_price']

# Dividindo os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definindo o modelo XGBoost com os melhores hiperparâmetros encontrados
model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=1000,  # Número de árvores
    learning_rate=0.05,  # Taxa de aprendizado
    max_depth=6,  # Profundidade máxima das árvores
    min_child_weight=3,  # Peso mínimo de uma folha
    subsample=0.8,  # Subamostragem
    colsample_bytree=0.8,  # Amostragem das colunas por árvore
    gamma=0.2,  # Complexidade da árvore
    reg_alpha=0.1,  # Regularização L1
    reg_lambda=1,  # Regularização L2
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Avaliação do modelo
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"R2 Score: {r2}")

# Salvando o modelo para uso posterior
import joblib
joblib.dump(model, 'xgboost_model.pkl')
