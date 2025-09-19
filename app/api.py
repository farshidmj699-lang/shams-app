from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ai_service import analyze_audio, synthesize_light
from app.models.schemas import SynthesizePrompt

router = APIRouter()

@router.post('/analyze')
async def analyze_audio_route(file: UploadFile = File(...)):
    if not file.content_type.startswith('audio/'):
        raise HTTPException(400, detail="Invalid audio file")
    
    audio_bytes = await file.read()
    result = analyze_audio(audio_bytes)
    return {"ok": True, "result": result}

@router.post('/synthesize')
async def synthesize_light_route(prompt: SynthesizePrompt):
    light_params = synthesize_light(prompt.dict())
    return {"ok": True, "light_params": light_params}