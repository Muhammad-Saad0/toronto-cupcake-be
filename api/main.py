from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import FastAPI, BackgroundTasks
from helper_functions import send_email_async
from routes.cupcake import router as cupcakes_router
from routes.checkout import router as checkout_router
from fastapi.middleware.cors import CORSMiddleware
from settings import Envs
import smtplib

app = FastAPI()

origins = [
    Envs.FRONTEND_URL,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Allow specific origins
    allow_credentials=True,         # Allow cookies and other credentials
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)

app.include_router(cupcakes_router, prefix="/cupcake", tags=["cupcakes"])
app.include_router(checkout_router, prefix="/checkout", tags=["checkout"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cupcake API!"}

port = 2525
host = "smtp.mailmug.net"
login = "bmt6unxndmelub3t"
password = "dgrzr7d9plovydyj"

sender_email = "doritozz349@gmail.com"
to_email = "saadmahbobb00@proton.me"
message = MIMEMultipart("alternative")

message["from"] = sender_email
message["to"] = to_email
message["subject"] = "hello world"

@app.get("/send-email",)
def send_email():
    html = "<h1>helloo world!!!</h1>"
    part = MIMEText(html, "html")
    message.attach(part)
    
    server = smtplib.SMTP(host, 2525)
    server.set_debuglevel(1)
    server.esmtp_features["auth"] = "LOGIN PLAIN"
    server.login(login, password)
    server.sendmail(sender_email, to_email, message.as_string())
    