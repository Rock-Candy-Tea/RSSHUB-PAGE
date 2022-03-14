
---
title: 'Vue通过vue-cli3.0图形化Vue-ui创建项目到优化部署项目'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3735156-d8d4d7111fc23bfd.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3735156-d8d4d7111fc23bfd.png'
---

<div>   
<h4>简介</h4>
<p>vue-cli 是一个官方发布 vue.js 项目脚手架，使用 vue-cli 可以快速创建 vue 项目。工具就是为了让开发者能够开箱即用快速地进行应用开发而开发的，可以通过vue create命令行的方式创建vue项目，也可以使用vue ui图形化的方式创建vue项目。本篇文章主要讲解使用vue ui图形化方式来创建vue项目。</p>
<h4>优点</h4>
<ul>
<li>不需要使用繁琐的命令行来操作；</li>
<li>直观高效的安装插件和依赖；</li>
<li>对打包后的项目直观查看资源文件和分析项目。</li>
</ul>
<p><strong>案例地址:</strong><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fpengjunshan%2FWebPJS" target="_blank">https://github.com/pengjunshan/WebPJS</a></p>
<p><strong>其它Web文章</strong><br>
<a href="https://www.jianshu.com/p/f91828123a28" target="_blank">CSS浮动的使用和解决浮动的五种方法</a><br>
<a href="https://www.jianshu.com/p/634d820dd6a5" target="_blank">CSS定位relative、absolute、fixed使用总结</a><br>
<a href="https://www.jianshu.com/p/760b64e2bc11" target="_blank">原生开发WebApi知识点总结</a><br>
<a href="https://www.jianshu.com/p/48fb1b0cd6f5" target="_blank">开发中常用jQuery知识点总结</a><br>
<a href="https://www.jianshu.com/p/37fd2c60fb1b" target="_blank">C3动画+H5知识点使用总结</a><br>
<a href="https://www.jianshu.com/p/02b465b59d5d" target="_blank">Flex布局知识点总结</a><br>
<a href="https://www.jianshu.com/p/bbe8fd6a20a0" target="_blank">ES6常用知识总结</a><br>
<a href="https://www.jianshu.com/p/72332db06a23" target="_blank">Vue学习知识总结</a><br>
<a href="https://www.jianshu.com/p/16b5ff963819" target="_blank">开发环境到生产环境配置webpack</a><br>
待续......</p>
<h4>前提</h4>
<h6>Node.js版本</h6>
<blockquote>
<p>Node.js版本必须是8.9 或更高版本,通过node -v命令行查看本地node的版本,如版本小于8.9只需更新node版本即可。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="538" data-height="67"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-d8d4d7111fc23bfd.png" data-original-width="538" data-original-height="67" data-original-format="image/png" data-original-filesize="1026" src="https://upload-images.jianshu.io/upload_images/3735156-d8d4d7111fc23bfd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>vue-cli版本</h6>
<blockquote>
<p>vue-cli版本必须是3.0或更高版本，通过vue -V命令行查看本地vue-cli的版本，如果版本小于3.0需要先通过 npm uninstall vue-cli -g 或 yarn global remove vue-cli 卸载它，然后在通过npm install -g @vue/cli 或 yarn global add @vue/cli再安装它。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="536" data-height="66"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-5b6df7ea1e34d3e2.png" data-original-width="536" data-original-height="66" data-original-format="image/png" data-original-filesize="1138" src="https://upload-images.jianshu.io/upload_images/3735156-5b6df7ea1e34d3e2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>创建项目</h4>
<h6>1.使用vue ui命令行启动可视化程序</h6>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="538" data-height="78"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-85d3f8d19aee76a3.png" data-original-width="538" data-original-height="78" data-original-format="image/png" data-original-filesize="1698" src="https://upload-images.jianshu.io/upload_images/3735156-85d3f8d19aee76a3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>2.打开可视化界面</h6>
<blockquote>
<p>复制生成的<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A8000" target="_blank">http://localhost:8000</a>地址到浏览器中打开，如果不是第一次使用，会默认上一次使用的项目。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1361" data-height="599"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-183b594675587742.png" data-original-width="1361" data-original-height="599" data-original-format="image/png" data-original-filesize="52472" src="https://upload-images.jianshu.io/upload_images/3735156-183b594675587742.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>3.创建新项目</h6>
<blockquote>
<p>首先点击左上角项目倒三角，弹窗底部有个Vue项目管理器，点击它进入创建项目页面。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1357" data-height="460"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-15e6ab60a87da3f9.png" data-original-width="1357" data-original-height="460" data-original-format="image/png" data-original-filesize="50480" src="https://upload-images.jianshu.io/upload_images/3735156-15e6ab60a87da3f9.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>4.选择创建项目目录</h6>
<blockquote>
<p>首先点击创建按钮，然后选择创建项目的地址，点击下方在此创建新项目。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1363" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-e500d2aeb75413a5.png" data-original-width="1363" data-original-height="596" data-original-format="image/png" data-original-filesize="36457" src="https://upload-images.jianshu.io/upload_images/3735156-e500d2aeb75413a5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>5.创建项目名称</h6>
<blockquote>
<p>填写项目文件夹，包管理器一般默认就行。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1363" data-height="595"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-3c246679ac372151.png" data-original-width="1363" data-original-height="595" data-original-format="image/png" data-original-filesize="35292" src="https://upload-images.jianshu.io/upload_images/3735156-3c246679ac372151.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>6.选择预设</h6>
<blockquote>
<p>建议选择手动</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1363" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-3424b00d0c176c21.png" data-original-width="1363" data-original-height="596" data-original-format="image/png" data-original-filesize="28139" src="https://upload-images.jianshu.io/upload_images/3735156-3424b00d0c176c21.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>7.选择安装的插件</h6>
<blockquote>
<p>Babel是默认必选的，跳转肯定需要Router，所以Router也选上，ESLint用来规范代码的，选中“使用配置文件”可以将插件的配置保存在各自的配置文件中。这里根据自身项目需要来选择插件是否安装，比如Vuex需要就选中不需要就不选。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1362" data-height="597"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-610a3bc24a045a0e.png" data-original-width="1362" data-original-height="597" data-original-format="image/png" data-original-filesize="43974" src="https://upload-images.jianshu.io/upload_images/3735156-610a3bc24a045a0e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1365" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-727bb0b6412a6e7e.png" data-original-width="1365" data-original-height="596" data-original-format="image/png" data-original-filesize="47879" src="https://upload-images.jianshu.io/upload_images/3735156-727bb0b6412a6e7e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>8.配置</h6>
<blockquote>
<p>一般需要选中把router设置为history,因为后端也要处理；选择ESLint的模式，选中ESLint-Standard标准模式；然后选择save保存的时候校验。然后点击下方创建项目按钮。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1364" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-853ad820dbbdcc88.png" data-original-width="1364" data-original-height="596" data-original-format="image/png" data-original-filesize="47661" src="https://upload-images.jianshu.io/upload_images/3735156-853ad820dbbdcc88.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</blockquote>
<h6>9.开始创建项目</h6>
<blockquote>
<p>个人认为小白不建议保存预设，多操作几次不是更加有印象吗</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1364" data-height="597"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-f4d6e68eeb9dd684.png" data-original-width="1364" data-original-height="597" data-original-format="image/png" data-original-filesize="50595" src="https://upload-images.jianshu.io/upload_images/3735156-f4d6e68eeb9dd684.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1365" data-height="483"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-60f56340d9653df7.png" data-original-width="1365" data-original-height="483" data-original-format="image/png" data-original-filesize="32124" src="https://upload-images.jianshu.io/upload_images/3735156-60f56340d9653df7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>10.项目创建完成  仪盘表</h6>
<blockquote>
<p>等项目创建完成后自动切换到当前项目</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1366" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-4a4e044e0223d8c1.png" data-original-width="1366" data-original-height="596" data-original-format="image/png" data-original-filesize="47372" src="https://upload-images.jianshu.io/upload_images/3735156-4a4e044e0223d8c1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>11.安装插件 以Element-ui（PC端UI库）为例</h6>
<ul>
<li>
<p>点击左侧菜单的插件按钮，可以查看项目中所用到的所有插件</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1361" data-height="425"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-4eed9dbf12875c19.png" data-original-width="1361" data-original-height="425" data-original-format="image/png" data-original-filesize="42156" src="https://upload-images.jianshu.io/upload_images/3735156-4eed9dbf12875c19.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
<li>
<p>点击上图右上角的安装插件进入查找插件页面，输入框内输入要安装的插件名称，选中你要安装的插件后点击右下方的安装按钮进行安装插件。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1362" data-height="598"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-664cbc49722a4bb7.png" data-original-width="1362" data-original-height="598" data-original-format="image/png" data-original-filesize="76787" src="https://upload-images.jianshu.io/upload_images/3735156-664cbc49722a4bb7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
<li>
<p>插件安装完成后点击Fully import选择框，选择Import on demand按需导入。然后点击完成安装。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1365" data-height="601"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-c0d3e463c95f2f1c.png" data-original-width="1365" data-original-height="601" data-original-format="image/png" data-original-filesize="43777" src="https://upload-images.jianshu.io/upload_images/3735156-c0d3e463c95f2f1c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
</ul>
<h6>12.安装项目依赖 以Axios（Vue官方推荐的网络请求）为例</h6>
<ul>
<li>
<p>点击左侧依赖菜单，进入项目依赖页。可以看到所有的运行依赖和开发依赖。每个依赖项后都有个删除按钮，可以手动点击删除当前依赖。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1364" data-height="598"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-a886e1f39cdc1e24.png" data-original-width="1364" data-original-height="598" data-original-format="image/png" data-original-filesize="48177" src="https://upload-images.jianshu.io/upload_images/3735156-a886e1f39cdc1e24.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
<li>
<p>点击上图右上角安装依赖按钮进入搜索页面，输入项目需要的依赖然后选中后点击下方安装按钮。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1363" data-height="594"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-9de30364f0331797.png" data-original-width="1363" data-original-height="594" data-original-format="image/png" data-original-filesize="81391" src="https://upload-images.jianshu.io/upload_images/3735156-9de30364f0331797.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
</ul>
<h6>13.配置项</h6>
<ul>
<li>这里可以配置一些基础设置和CSS的一些设置</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1361" data-height="593"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-2396fe4956bb0d4c.png" data-original-width="1361" data-original-height="593" data-original-format="image/png" data-original-filesize="51658" src="https://upload-images.jianshu.io/upload_images/3735156-2396fe4956bb0d4c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>14.任务 serve</h6>
<ul>
<li>
<p>serve 开发环境，点击运行按钮，等项目编译完后点击启动app按钮后自动开发项目 。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1364" data-height="595"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-7a8d387b85b7f345.png" data-original-width="1364" data-original-height="595" data-original-format="image/png" data-original-filesize="66849" src="https://upload-images.jianshu.io/upload_images/3735156-7a8d387b85b7f345.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1348" data-height="574"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-6af2c98867a3d4db.png" data-original-width="1348" data-original-height="574" data-original-format="image/png" data-original-filesize="27856" src="https://upload-images.jianshu.io/upload_images/3735156-6af2c98867a3d4db.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
</li>
</ul>
<h6>15.vue-cli3.0项目目录</h6>
<blockquote>
<p>和2.0版本相比少了很多配置</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="668" data-height="451"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-397ffcbb38b19fda.png" data-original-width="668" data-original-height="451" data-original-format="image/png" data-original-filesize="31956" src="https://upload-images.jianshu.io/upload_images/3735156-397ffcbb38b19fda.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h6>16.任务 build</h6>
<blockquote>
<p>我们点击build的运行按钮，进行打包项目，打包完成后往下滑可以查看资源和依赖库文件的大小，还会在项目目录中生成一个dist文件夹就是打包后的成果。</p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1364" data-height="596"><img data-original-src="//upload-images.jianshu.io/upload_images/3735156-51d80a29563c47b0.png" data-original-width="1364" data-original-height="596" data-original-format="image/png" data-original-filesize="55161" src="https://upload-images.jianshu.io/upload_images/3735156-51d80a29563c47b0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h4>优化项目</h4>
<h6>1.添加进度条</h6>
<blockquote>
<p>给项目添加进度条效果，先打开项目控制台，打开依赖，安装nprogress，打开main.js，编写如下代码</p>
</blockquote>
<pre><code>//导入进度条插件
import NProgress from 'nprogress'
//导入进度条样式
import 'nprogress/nprogress.css'
.....
//请求在到达服务器之前，先会调用use中的这个回调函数来添加请求头信息
axios.interceptors.request.use(config => &#123;
  //当进入request拦截器，表示发送了请求，我们就开启进度条
  NProgress.start()
  //为请求头对象，添加token验证的Authorization字段
  config.headers.Authorization = window.sessionStorage.getItem("token")
  //必须返回config
  return config
&#125;)
//在response拦截器中，隐藏进度条
axios.interceptors.response.use(config =>&#123;
  //当进入response拦截器，表示请求已经结束，我们就结束进度条
  NProgress.done()
  return config
&#125;)
</code></pre>
<h6>2.build阶段移除所有的console信息</h6>
<blockquote>
<p>安装一个插件（babel-plugin-transform-remove-console）在项目build阶段移除所有的console信息，打开项目控制台，点击依赖->开发依赖，输入babel-plugin-transform-remove-console，安装插件。打开babel.config.js，编辑代码如下：</p>
</blockquote>
<pre><code>//项目发布阶段需要用到的babel插件
const productPlugins = []

//判断是开发还是发布阶段
if(process.env.NODE_ENV === 'production')&#123;
  //发布阶段
  productPlugins.push("transform-remove-console")
&#125;

module.exports = &#123;
  "presets": [
    "@vue/app"
  ],
  "plugins": [
    [
      "component",
      &#123;
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      &#125;
    ],
    ...productPlugins
  ]
&#125;
</code></pre>
<h6>3.修改webpack的默认配置</h6>
<blockquote>
<p>默认情况下，vue-cli 3.0生成的项目，隐藏了webpack配置项，如果我们需要配置webpack，需要通过vue.config.js来配置。在项目根目录中创建vue.config.js文件</p>
</blockquote>
<pre><code>module.exports = &#123;
    chainWebpack:config=>&#123;
        //发布模式
        config.when(process.env.NODE_ENV === 'production',config=>&#123;
            //entry找到默认的打包入口，调用clear则是删除默认的打包入口
            //add添加新的打包入口
            config.entry('app').clear().add('./src/main-prod.js')
        &#125;)
        //开发模式
        config.when(process.env.NODE_ENV === 'development',config=>&#123;
            config.entry('app').clear().add('./src/main-dev.js')
        &#125;)
    &#125;
&#125;
</code></pre>
<h6>4.加载外部CDN</h6>
<blockquote>
<p>默认情况下，依赖项的所有第三方包都会被打包到js/chunk-vendors.js文件中，导致该js文件过大;</p>
</blockquote>
<ul>
<li>可以在vue.config.js中通过externals排除这些包，使它们不被打包到js/chunk-vendors.js文件中</li>
</ul>
<pre><code>module.exports = &#123;
    chainWebpack:config=>&#123;
        //发布模式
        config.when(process.env.NODE_ENV === 'production',config=>&#123;
            //entry找到默认的打包入口，调用clear则是删除默认的打包入口
            //add添加新的打包入口
            config.entry('app').clear().add('./src/main-prod.js')

            //使用externals设置排除项
            config.set('externals',&#123;
                vue:'Vue',
                'vue-router':'VueRouter',
                axios:'axios',
                'element-ui': 'ElementUI',
                echarts:'echarts'
                ...根据自己项目中用到的库
            &#125;)
        &#125;)
        //开发模式
        config.when(process.env.NODE_ENV === 'development',config=>&#123;
            config.entry('app').clear().add('./src/main-dev.js')
        &#125;)
    &#125;
&#125;
</code></pre>
<ul>
<li>设置好排除之后，为了使我们可以使用vue，axios等内容，我们需要加载外部CDN的形式解决引入依赖项。打开开发入口文件main-prod.js,删除掉默认的引入代码</li>
</ul>
<h6>5.定制首页内容</h6>
<blockquote>
<p>开发环境的首页和发布环境的首页展示内容的形式有所不同;我们可以通过插件的方式来定制首页内容，打开vue.config.js，编写代码如下：</p>
</blockquote>
<pre><code>module.exports = &#123;
    chainWebpack:config=>&#123;
        config.when(process.env.NODE_ENV === 'production',config=>&#123;
            ......
            
            //使用插件
            config.plugin('html').tap(args=>&#123;
                //添加参数isProd
                args[0].isProd = true
                return args
            &#125;)
        &#125;)

        config.when(process.env.NODE_ENV === 'development',config=>&#123;
            config.entry('app').clear().add('./src/main-dev.js')

            //使用插件
            config.plugin('html').tap(args=>&#123;
                //添加参数isProd
                args[0].isProd = false
                return args
            &#125;)
        &#125;)
    &#125;
&#125;
</code></pre>
<blockquote>
<p>然后在public/index.html中使用插件判断是否为发布环境并定制首页内容;</p>
</blockquote>
<pre><code><!DOCTYPE html>
<html lang="en">
 <head>
   <meta charset="utf-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <link rel="icon" href="<%= BASE_URL %>favicon.ico">
   <title><%= htmlWebpackPlugin.options.isProd ? '' : 'dev - ' %>电商后台管理系统</title>

 </head>
 .......
</code></pre>
<h6>6.路由懒加载</h6>
<blockquote>
<p>当路由被访问时才加载对应的路由文件，就是路由懒加载。</p>
</blockquote>
<ul>
<li>1.安装 @babel/plugin-syntax-dynamic-import</li>
</ul>
<blockquote>
<p>打开vue控制台，点击依赖->安装依赖->开发依赖->搜索@babel/plugin-syntax-dynamic-import点击安装。</p>
</blockquote>
<ul>
<li>2.在babel.config.js中声明该插件，打开babel.config.js</li>
</ul>
<pre><code>//项目发布阶段需要用到的babel插件
const productPlugins = []

//判断是开发还是发布阶段
if(process.env.NODE_ENV === 'production')&#123;
  //发布阶段
  productPlugins.push("transform-remove-console")
&#125;

module.exports = &#123;
  "presets": [
    "@vue/app"
  ],
  "plugins": [
    [
      "component",
      &#123;
        "libraryName": "element-ui",
        "styleLibraryName": "theme-chalk"
      &#125;
    ],
    ...productPlugins,
    //配置路由懒加载插件
    "@babel/plugin-syntax-dynamic-import"
  ]
&#125;
</code></pre>
<ul>
<li>3.将路由更改为按需加载的形式，打开router.js，更改引入组件代码如下：</li>
</ul>
<pre><code>import Vue from 'vue'
import Router from 'vue-router'
const Login = () => import(/* webpackChunkName:"login_home_welcome" */ './components/Login.vue')
// import Login from './components/Login.vue'
const Home = () => import(/* webpackChunkName:"login_home_welcome" */ './components/Home.vue')
// import Home from './components/Home.vue'
......
</code></pre>
<h6>7.项目上线</h6>
<blockquote>
<p>通过node创建服务器,首先创建一个文件夹server(名字随便起)来存放node服务器，使用终端打开server文件夹，输入命令 npm init -y初始化包之后，输入命令 npm i express -S安装Express，然后打开我们项目目录，复制dist文件夹，粘贴到server文件夹中，在server文件夹中创建app.js文件,编写代码如下：</p>
</blockquote>
<pre><code>const express = require('express')
const app = express()
app.use(express.static('./dist'))
app.listen(8998,()=>&#123;
    console.log("server running at http://127.0.0.1:8998")
&#125;)
</code></pre>
<blockquote>
<p>然后再次在终端中输入  node app.js 然后在浏览器输入你的电脑的ip加端口就可以打开了。</p>
</blockquote>
<h6>8.使用pm2管理应用</h6>
<blockquote>
<p>当在本地通过命令行启动服务后，关闭命令窗口后服务就会自动关闭掉，是不是很气人！通过pm2就会避免这种情况；</p>
</blockquote>
<ul>
<li>1.打开server文件夹的终端，输入命令：npm i pm2 -g，安装pm2;</li>
<li>2.使用pm2启动项目，在终端中输入命令：pm2 start app.js --name 自定义名称,开启服务；</li>
<li>3.查看项目列表命令：pm2 ls；</li>
<li>4.重启项目：pm2 restart 自定义名称；</li>
<li>5.停止项目：pm2 stop 自定义名称；<br>
+6.删除项目：pm2 delete 自定义名称；</li>
</ul>
  
</div>
            