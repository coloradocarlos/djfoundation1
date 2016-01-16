var gulp = require('gulp');
var $    = require('gulp-load-plugins')();
var connect = require('gulp-connect');

var sassPaths = [
  'bower_components/foundation-sites/scss',
  'bower_components/motion-ui/src'
];

gulp.task('sass', function() {
  return gulp.src('scss/app.scss')
    .pipe($.sass({
      includePaths: sassPaths
    })
      .on('error', $.sass.logError))
    .pipe($.autoprefixer({
      browsers: ['last 2 versions', 'ie >= 9']
    }))
    .pipe(gulp.dest('css'))
    .pipe(connect.reload());
});

gulp.task('connect', function() {
   connect.server({
     livereload: true
   });
});

gulp.task('default', ['sass', 'connect'], function() {
  gulp.watch(['scss/**/*.scss'], ['sass']);
});
