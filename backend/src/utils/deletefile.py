import os
def delete_file(filepath:str):
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            return{
                "status":True,
                "message":"Successfully Deleted"
            }
        else:
            return{
                "status":False,
                "message":"File not found"
            }

    
    except Exception as e:
        return {
            "status":False
        }