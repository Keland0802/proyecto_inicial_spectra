from datetime import datetime
from fastapi import FastAPI, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from controller.user import User
from models.conexion import Conexion
from controller.Register import Register
from controller.Plan import Plan



from starlette.middleware.sessions import SessionMiddleware
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="12345")   


@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/searchId", response_class=HTMLResponse)
async def searchId(request: Request):
    return templates.TemplateResponse("searchId.html", {"request": request})


@app.get("/searchDate", response_class=HTMLResponse)
async def searchDate(request: Request):
    return templates.TemplateResponse("searchDate.html", {"request": request})



@app.get("/report", response_class=HTMLResponse)
async def report(request: Request):
    return templates.TemplateResponse("report.html", {"request": request})

@app.get("/blockade", response_class=HTMLResponse)
async def blockade(request: Request):
    return templates.TemplateResponse("blockade.html", {"request": request})


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/registerUser", response_class=HTMLResponse)
async def registerUser(request: Request):
    return templates.TemplateResponse("registerUser.html", {"request": request})

@app.get("/plan", response_class=HTMLResponse)
async def plan(request: Request):
    query="SELECT * FROM tipo_actividades"
    actividades=Conexion().consult(query)
    return templates.TemplateResponse("plan.html", {"request": request, "actividades": actividades})


@app.post("/createUser")
async def createUser(request: Request, name: str = Form(), id: str = Form()):
    
    user=User()
    verifyUser=user.verifyUser(id)
    
    if verifyUser:
        request.session["flash_message"] = {
                        "text": "Usuario ya registrado en el sistema, por favor ingrese con su número ya registrado", "type": "error"}

    else:
        newUser=user.createUser(name, id)
        if newUser:
            request.session["flash_message"] = {"text": "Registro exitoso", "type": "success"}

            
        else:
            request.session["flash_message"] = {"text": "Error al registrar el usuario, intente nuevamente", "type": "error"}
            return RedirectResponse(url="/registerUser", status_code=302)

    return RedirectResponse(url="/", status_code=302)  # Redirigir para evitar recarga con mensaje
            
            
@app.post("/login")
async def verifyUser (request: Request, id: str = Form()):
    
    user=User()
    verifyUser=user.verifyUser(id)
    if verifyUser:
        request.session["user"] = {"id": verifyUser[0], "name": verifyUser[1]}
        
        return templates.TemplateResponse("home.html", {"request": request})
    else:
        request.session["flash_message"] = {"text": "Usuario no registrado en el sistema, por favor si no está registrado ingrese al botón Sing Up para registrarse", "type": "error"}

    return RedirectResponse(url="/", status_code=302)  # Redirigir para evitar recarga con mensaje

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    query="SELECT * FROM tipo_actividades"
    actividades=Conexion().consult(query)
    return templates.TemplateResponse("register.html", {"request": request, "actividades": actividades})


@app.post("/registerPlan")
async def registerPlan (request: Request, type_act: str = Form(), description_act: str=Form(), num_proyect: str=Form(), hours: str=Form()):
    user = request.session.get("user")
    register= Plan()
    if num_proyect:
        proyect=num_proyect
    else:
        proyect=None
    
    comment="Sin bloqueos y/o problemas"
    
    regist= register.createPlan(user['id'], type_act, description_act, proyect, hours, comment)
    
    if regist:
                request.session["flash_message"] = {"text": "Registro exitoso", "type": "success"}
    else:
        request.session["flash_message"] = {"text": "No se pudo realizar el registro", "type": "error"}

    return RedirectResponse(url="/home", status_code=302)  # Redirigir para evitar recarga con mensaje
    
    
@app.post("/blockade")
async def blockade (request: Request, comment: str=Form()):
    user = request.session.get("user")
    register= Plan()
   
        
    if comment:
        pass
    else:
        comment="Sin bloqueos y/o problemas"
    
    regist= register.createBlockade(user['id'], comment)
    
    if regist:
               request.session["flash_message"] = {"text": "Registro exitoso", "type": "success"}
    else:
        request.session["flash_message"] = {"text": "No se pudo realizar el registro", "type": "error"}

    return RedirectResponse(url="/home", status_code=302)  # Redirigir para evitar recarga con mensaje
        
    
    

@app.post("/registerAct")
async def registerAct (request: Request, type_act: str = Form(), description_act: str=Form(), num_proyect: str=Form(), hours: str=Form(),
                        date: str=Form(), comment: str=Form()):
    user = request.session.get("user")
    register= Register()
    if num_proyect:
        proyect=num_proyect
    else:
        proyect=None
        
    if comment:
        pass
    else:
        comment="Sin bloqueos y/o problemas"
    
    regist= register.createRegister(user['id'], type_act, description_act, proyect, hours, date, comment)
    
    if regist:
                request.session["flash_message"] = {"text": "Registro exitoso", "type": "success"}
    else:
                request.session["flash_message"] = {"text": "No se pudo realizar el registro", "type": "error"}

    return RedirectResponse(url="/home", status_code=302)  # Redirigir para evitar recarga con mensaje
        
           
@app.get("/logout")
async def logout(request: Request):
    request.session.clear()  
    return RedirectResponse(url="/", status_code=302)


@app.get("/reports", response_class=HTMLResponse)
async def report(request: Request):
    
    query = """SELECT 
                p.id_planeacion,
                p.cedula_usu,
                ta.nombre_tipo_actividad AS actividad,
                p.descripcion_act,
                p.num_proyecto,
                p.horas,
                p.fecha,
                p.comentario
            FROM 
                planeacion_actividades p
            LEFT JOIN 
                tipo_actividades ta 
            ON 
                p.actividad = ta.id_tipo_actividad"""
    plan=Conexion().consult(query)
    
    
    query2 = """SELECT 
                r.id_registro,
                r.cedula_usu,
                ta.nombre_tipo_actividad AS actividad,
                r.descripcion_act,
                r.num_proyecto,
                r.horas,
                r.fecha,
                r.comentario
            FROM 
                registro_actividades r
            JOIN 
                tipo_actividades ta 
            ON 
                r.actividad = ta.id_tipo_actividad"""
    regist = Conexion().consult(query2)

    
    return templates.TemplateResponse("report.html", {"request": request, "registros": regist,"planeacion": plan})




@app.get("/filterId", response_class=HTMLResponse)
async def filterId(request: Request, id: str=Query(...)):
    
        query = """SELECT 
                    r.id_registro,
                    r.cedula_usu,
                    ta.nombre_tipo_actividad AS actividad,
                    r.descripcion_act,
                    r.num_proyecto,
                    r.horas,
                    r.fecha,
                    r.comentario
                FROM 
                    registro_actividades r
                LEFT JOIN 
                    tipo_actividades ta 
                ON 
                    r.actividad = ta.id_tipo_actividad
                WHERE r.cedula_usu=%s"""
        params = (id,)
        regist = Conexion().consult(query, params)
       
        query2 = """SELECT 
                    p.id_planeacion,
                    p.cedula_usu,
                    ta.nombre_tipo_actividad AS actividad,
                    p.descripcion_act,
                    p.num_proyecto,
                    p.horas,
                    p.fecha,
                    p.comentario
                FROM 
                    planeacion_actividades p
                LEFT JOIN 
                    tipo_actividades ta 
                ON 
                    p.actividad = ta.id_tipo_actividad
                WHERE p.cedula_usu=%s"""
        plan = Conexion().consult(query2, params)
      

        return templates.TemplateResponse("report.html", {"request": request, "registros": regist,"planeacion": plan})
    
    



@app.get("/filterDate", response_class=HTMLResponse)
async def filterDate(request: Request, start_date: str = Query(...),  end_date: str = Query(...)):
    
        date_format = "%Y-%m-%d"  # Por ejemplo, "2025-02-05"

        start_date_obj = datetime.strptime(start_date, date_format)
        end_date_obj = datetime.strptime(end_date, date_format)

        if start_date_obj > end_date_obj:
                request.session["flash_message"] = {"text": "La fecha de inicio no puede ser mayor que la fecha de final.","type": "error"}
                return RedirectResponse(url="/searchDate", status_code=302)  # Redirigir para evitar recarga con mensaje

    
        query = """SELECT 
                        r.id_registro,
                        r.cedula_usu,
                        ta.nombre_tipo_actividad AS actividad,
                        r.descripcion_act,
                        r.num_proyecto,
                        r.horas,
                        r.fecha,
                        r.comentario
                    FROM 
                        registro_actividades r
                    LEFT JOIN 
                        tipo_actividades ta 
                    ON 
                        r.actividad = ta.id_tipo_actividad
                    WHERE fecha BETWEEN %s AND %s"""
        params = (start_date, end_date)
        regist = Conexion().consult(query, params)
       
        query2 = """SELECT 
                        p.id_planeacion,
                        p.cedula_usu,
                        ta.nombre_tipo_actividad AS actividad,
                        p.descripcion_act,
                        p.num_proyecto,
                        p.horas,
                        p.fecha,
                        p.comentario
                    FROM 
                        planeacion_actividades p
                    LEFT JOIN 
                        tipo_actividades ta 
                    ON 
                        p.actividad = ta.id_tipo_actividad
                    WHERE fecha BETWEEN %s AND %s"""
        plan = Conexion().consult(query2, params)
      

        return templates.TemplateResponse("report.html", {"request": request, "registros": regist,"planeacion": plan})


@app.get("/clear_flash_message")
async def clear_flash_message(request: Request):
    request.session.pop("flash_message", None)  # Eliminar el mensaje de la sesión
    return {"message": "Flash message cleared"}  # Respuesta JSON
