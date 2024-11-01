def init(celery_app, **global_decorators):
    @celery_app.task
    def get_subs(url: str):
        from tasks.packs.subtitles.resources import downloader as dl_module
        from tasks.packs.subtitles.resources import whisper as whisper_module
        output_path = "/tmp/audio.mp3"
        dl_module.download_audio(url=url, output_path=output_path)
        
        language_info, transcription = whisper_module.transcribe_video(input_file=output_path)
        
        return {
            "language_info": language_info,
            "transcription": transcription
        }