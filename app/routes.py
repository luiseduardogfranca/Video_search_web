from flask import Blueprint
from flask import request
from flask import render_template
from app.video_url.core import Page_video
from app import settings

bp = Blueprint("routes",__name__, "/")

@bp.route("/", methods=("GET","POST"))
def index():
    if request.method == 'POST':
        try:
            search_text = request.form["Search_box"]
            videos=Page_video.search_videos(search_text)
            if(len(videos) == 1):
                col_size = 6
                offset_size = 3
            else:
                col_size = int(12/len(videos))
                offset_size = 0
        except Exception as e:
            if settings.DEBUG:
                return render_template("index.html",error=e)
                


        return render_template("index.html", videos = videos, col_size = col_size, offset_size = offset_size)

    return render_template("index.html")
