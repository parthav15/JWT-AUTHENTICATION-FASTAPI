from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from schemas import Login, Refresh, Register, Token, User
from services import add_user, get_user
from utils import verify_password

router = APIRouter()


@router.post("/login")
def login(user: Token, authorize: AuthJWT = Depends()):
    try:
        if not user.username or not user.password:
            raise HTTPException(status_code=400, detail={"success": False, "message": "Username and password required"})

        db_user = get_user(user.username)
        if not db_user:
            raise HTTPException(status_code=404, detail={"success": False, "message": "User not found"})

        if not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=401, detail={"success": False, "message": "Invalid password"})

        access_token = authorize.create_access_token(subject=user.username)
        refresh_token = authorize.create_refresh_token(subject=user.username)

        return {"success": True, "message": "Logged in successfully", "data": {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}}, 200

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={"success": False, "message": "Internal server error"})


@router.post("/refresh")
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"success": True, "message": "Refreshed token", "data": {"access_token": new_access_token, "token_type": "bearer"}}, 200


@router.get("/me")
def protected(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    current_user = authorize.get_jwt_subject()
    user = get_user(current_user)
    return {"success": True, "message": "Current user", "data": User(**user.__dict__)}, 200


@router.post("/register")
def protected(user: Register):
    new_user = Register(
        username=user.username,
        password=user.password,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        address=user.address,
        phone_number=user.phone_number
    )
    user = add_user(new_user)
    return {"success": True, "message": "User created successfully", "data": User(**user.__dict__)}, 201
