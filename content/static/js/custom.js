function readURL(uploader) {
    $('.update_img').attr('src',
        window.URL.createObjectURL(uploader.files[0]));
};