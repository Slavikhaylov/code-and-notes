from pathlib import Path
from django.conf import settings


from django.core.files.storage import FileSystemStorage


def check_if_stem_exist(storage, file_path: Path, c_count):
    aviable_extension ={
        'popular': [
            '.apng', '.avif', '.gif', '.jpeg', '.jpg', '.png', '.svg', '.webp', '.bmp', '.ico', '.tiff',],
        'all':['.blp', '.bmp', '.dib', '.bufr', '.cur', '.pcx', '.dcx', '.dds', '.ps', '.eps', '.fit',
            '.fits', '.fli', '.flc', '.ftc', '.ftu', '.gbr', '.gif', '.grib', '.h5', '.hdf', '.png',
            '.apng', '.jp2', '.j2k', '.jpc', '.jpf', '.jpx', '.j2c', '.icns', '.ico', '.im', '.iim',
            '.tif', '.tiff', '.jfif', '.jpe', '.jpg', '.jpeg', '.mpg', '.mpeg', '.mpo', '.msp',
            '.palm', '.pcd', '.pdf', '.pxr', '.pbm', '.pgm', '.ppm', '.pnm', '.psd', '.bw', '.rgb',
            '.rgba', '.sgi', '.ras', '.tga', '.icb', '.vda', '.vst', '.webp', '.wmf', '.emf', '.xbm',
            '.xpm']
    }

    file_name = str(file_path.parent / Path(file_path.stem))
    if c_count != 0:
        for ext in aviable_extension['popular']:
            if storage.exists(f"{file_name}_{c_count}{ext}") or storage.exists(f"{file_name}_{c_count}{ext.upper()}") :
                return True
    else:
        for ext in aviable_extension['popular']:
            if ext == file_path.suffix or ext.upper() == file_path.suffix :
                continue
            if storage.exists(file_path.with_suffix(ext)) or storage.exists(file_path.with_suffix(ext.upper())):
                return True
    return False


def rename_picture_in_db(model_class, obj_field):
    for obj in model_class.objects.all():
        picture = getattr(obj,  obj_field, None)
        
        if not picture:
            continue
        c_count = 0
        picture_path = Path(picture.path)
        path_name = Path(picture.name)
        file_extension = path_name.suffix
        while check_if_stem_exist(FileSystemStorage(), path_name, c_count):
            c_count+=1
        if c_count != 0:
            path_name = f"{str(path_name.parent / Path(path_name.stem))}_{c_count}{file_extension}" 
            new_path = Path(settings.MEDIA_ROOT) / path_name
            picture_path.rename(new_path)
            setattr(obj, obj_field, path_name)
            obj.save()
            print(path_name)


from app.v2.tiffest2.models import Movies, WorldMovies, News, Partners, Sponsors, WorldPeople, \
    History, HistoryPhoto, HistoryContest, HistoryGuest , HistoryLaureate, HistoryOpenCloseMovies, \
    HistoryPartners, MassMediaAboutUs, Celebrity, MovieScreening, Location, Premier


def launch():
    rename_picture_in_db(Movies, 'poster')
    rename_picture_in_db(WorldMovies, 'poster')
    rename_picture_in_db(News, 'image')
    rename_picture_in_db(Partners, 'image')
    rename_picture_in_db(Sponsors, 'image')
    rename_picture_in_db(WorldPeople, 'photo')
    rename_picture_in_db(History, 'image')
    rename_picture_in_db(HistoryPhoto, 'photo')
    rename_picture_in_db(HistoryContest, 'image')
    rename_picture_in_db(HistoryGuest, 'photo')
    rename_picture_in_db(HistoryLaureate, 'poster')
    rename_picture_in_db(HistoryOpenCloseMovies, 'poster')
    rename_picture_in_db(HistoryPartners, 'image')
    rename_picture_in_db(MassMediaAboutUs, 'photo')
    rename_picture_in_db(Celebrity, 'image')
    rename_picture_in_db(MovieScreening, 'image')
    rename_picture_in_db(Location, 'image')
    rename_picture_in_db(Premier, 'image')




