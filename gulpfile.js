//食用方法
//把这个放在hexo的根目录
//先装cnpm  -->  npm install -g cnpm --registry=https://registry.npm.taobao.org
//然后 --> cnpm install -g gulp
//然后 --> cnpm install gulp gulp-htmlclean gulp-htmlmin gulp-clean-css gulp-uglify-es gulp-imagemin del gulp-minify-inline-json --save-dev
//修改img路径为你的source中实际的图片存储路径
//准备上传时 直接输入 gulp

var gulp = require('gulp');
var minifycss = require('gulp-clean-css');
var uglify = require('gulp-uglify-es').default;
var htmlmin = require('gulp-minify-html');
var htmlclean = require('gulp-htmlclean');
var imagemin = require('gulp-imagemin');
var del = require('del');
var Hexo = require('hexo');
var minifyInlineJSON = require('gulp-minify-inline-json');

gulp.task('clean', function () {
    return del(['public/**/*']);
});

var hexo = new Hexo(process.cwd(), {});
gulp.task('generate', function (cb) {
    hexo.init().then(function () {
        return hexo.call('generate', {
            watch: false
        });
    }).then(function () {
        return hexo.exit();
    }).then(function () {
        return cb()
    }).catch(function (err) {
        console.log(err);
        hexo.exit(err);
        return cb(err);
    })
});

gulp.task('deploy', function () {
    return hexo.init().then(function () {
        return hexo.call('deploy', {
            watch: false
        }).then(function () {
            return hexo.exit();
        }).catch(function (err) {
            return hexo.exit(err);
        });
    });
});

gulp.task('minify-css', function () {
    return gulp.src('./public/**/*.css')
        .pipe(minifycss({
            compatibility: 'ie8'
        }))
        .pipe(gulp.dest('./public'));
});

gulp.task('minify-html', function () {
    return gulp.src('./public/**/*.html')
        .pipe(htmlclean())
        .pipe(htmlmin())
        .pipe(gulp.dest('./public'))
});


gulp.task('minify-images', async () => { 
  gulp.src('./public/images/**/*.*')//修改这里的路径
    .pipe(imagemin({
      optimizationLevel: 5, // 類型：Number  預設：3  取值範圍：0-7（優化等級）
      progressive: true, // 類型：Boolean 預設：false 無失真壓縮jpg圖片
      interlaced: false, // 類型：Boolean 預設：false 隔行掃描gif進行渲染
      multipass: false // 類型：Boolean 預設：false 多次優化svg直到完全優化
    }))
    .pipe(gulp.dest('./public/images'))//修改这里的路径
});

gulp.task('minify-js', function () {
    return gulp.src('./public/**/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('./public'));
});

gulp.task('minifyInlineJSON', function () {
    return gulp.src('./public/**/*.html')
        .pipe(minifyInlineJSON())
        .pipe(gulp.dest('./public'));
});

gulp.task('compress', gulp.series( 'minify-html','minify-css', 'minify-js', 'minifyInlineJSON'));

gulp.task('default', gulp.series('compress' ));
