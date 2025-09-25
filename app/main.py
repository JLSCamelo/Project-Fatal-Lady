from fastapi import FastAPI
from controllers import *
from routes.produto_route import *


app = FastAPI(title="Loja de Sapatos")

# Registrar rotas
app.include_router(router)    