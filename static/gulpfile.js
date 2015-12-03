'use strict';

var gulp = require('gulp'),
    gutil = require('gulp-util'),
    del = require('del'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('gulp-autoprefixer'),
    uglifyCSS = require('gulp-uglifycss'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    livereload = require('gulp-livereload');

gulp.task('clean', function () {
    del(['build/css/*', 'build/js/*']);
});

gulp.task('sass', function () {
    gulp.src([
            'scss/main.scss'
        ])
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', gutil.log))
        .pipe(autoprefixer({
            browsers: ['last 2 versions', 'ie 10']
        }))
        .pipe(uglifyCSS())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('build/css'))
        .pipe(livereload());
});

gulp.task('scripts', function () {
    gulp.src([
            'node_modules/foundation-apps/js/angular/foundation.js',
        ])
        .pipe(concat('main.js'))
        .pipe(uglify().on('error', gutil.log))
        .pipe(gulp.dest('build/js'))
        .pipe(livereload());
});

gulp.task('watch', function () {
    gulp.watch('js/*.js', ['scripts']);
    gulp.watch(['scss/*.scss', 'scss/**/*.scss'], ['sass']);
    livereload.listen();
});

gulp.task('default', ['clean', 'sass', 'scripts', 'watch']);
