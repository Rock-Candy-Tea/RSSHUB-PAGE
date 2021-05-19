
---
title: 'UniAdmin 零前端代码通用后台 1.0.0 正式版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://cdn.jsdelivr.net/gh/ijry/sbase/image/uniadmin/ui4-1.png'
author: 开源中国
comments: false
date: Tue, 18 May 2021 19:14:00 GMT
thumbnail: 'https://cdn.jsdelivr.net/gh/ijry/sbase/image/uniadmin/ui4-1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start"><img src="https://cdn.jsdelivr.net/gh/ijry/sbase/image/uniadmin/ui4-1.png" referrerpolicy="no-referrer"></h2> 
<p><img alt height="455" src="https://oscimg.oschina.net/oscnet/up-8a8ee9109816748238028d14fa2d05e8f3b.png" width="800" referrerpolicy="no-referrer"></p> 
<p><img alt height="435" src="https://oscimg.oschina.net/oscnet/up-412515afaa8ed87e9fb9335d34d9b709dbc.png" width="800" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start">1.0.0正式版更新日志</h2> 
<p>【修复】修复列表弹窗打开不生效问题<br> 【修复】修复列表按钮样式配置<br> 【修复】修复模块列表右侧按钮错误<br> 【新增】FormBuilder补充setConfig方法<br> 【修复】防止权限管理时未勾选相关接口导致菜单不显示<br> 【优化】setStatus改为editField方法并新增继承机制，便于各个控制器里继承后加强自己的安全限制。<br> 【更新】更新文档新地址<br> 【优化】去除内置API文档功能推荐采用Sawgger规范<br> 【修复】修复安装第四步语法问题<br> 【新增】ListBuilder新增addTopButtons、addRightButtons和addColums方法<br> 【新增】支持表单项目联动显隐<br> 【新增】新增远程自定义组件支持<br> 【变更】对云后台1.0.0版本的支持<br> 【新增】支持自定义Form组件来满足系统内置组件不符合业务需要的场景，可以不用自定义整个页面组件了。<br> 【新增】自定义页面组件支持在列表里弹窗打开远程组件<br> 【新增】自定义页面组件支持传递参数给远程组件</p> 
<p>重要：我们正在内测thinkphp6.0版本，将不久推出。</p> 
<h2 style="text-align:start">简介</h2> 
<p style="text-align:start">UniAdmin是一套渐进式模块化开源后台，采用前后端分离技术，数据交互采用json格式，功能低耦合高内聚；核心模块支持系统设置、权限管理、用户管理、菜单管理、API管理等功能，后期上线模块商城将打造类似composer、npm的开放式插件市场；同时我们将打造一套兼容性的API标准，从ThinkPHP+Vue2开始，逐步覆盖laravel、spring-boot、django、yii、koa、react等多语言框架。</p> 
<h2 style="text-align:start">特性</h2> 
<h3 style="text-align:start">模块化</h3> 
<p style="text-align:start">UniAdmin后台本着高内聚低耦合的原则， 模块作为UniAdmin的最小功能包可以共享 用户可以在模块市场上传下载模块</p> 
<h3 style="text-align:start">Builder动态页面构建</h3> 
<p style="text-align:start">UniAdmin首创自主研发了基于前后端分离的第二代页面自动生成技术，目前支持list、form、info、tab、stack等Builder类型，自动生成列表、自动 生成表单等等都能很容易完成，二者结合可以完成90%以上的 后台功能需求。</p> 
<h2 style="text-align:start">多平台支持</h2> 
<p style="text-align:start">UniAdmin诞生在移动互联网后半场，面多各种 流量入口，UniAdmin将从如下方面对多个平台支持： pc端采用web方式实现，手机端将采用uni-app技术， 达到一次开发全面覆盖iOS、安卓、微信小程序、支 付宝小程序、百度小程序、头条小程序、H5，从而 节省开发者的大量精力。</p> 
<h3 style="text-align:start">多语言API兼容</h3> 
<p style="text-align:start">UniAdmin后台将打造统一的后台框架体系， 后端横跨php、java、python、node、.net 等等语言，前端将支持vue、react、angular 语言，多个语言支持通过统一的API标准兼容， 同时UniAdmin将从tp5+vue版本做起，先建立 API标准及示例，后期吸收优秀的志愿者加入 不同语言是实现开发</p> 
<p style="text-align:left">附录：云后台1.0.0能力更新：</p> 
<p style="text-align:start">【新增】弹窗支持高度与点击遮罩是否关闭选项</p> 
<p style="text-align:start">【新增】TinyMCE新增135编辑器插件</p> 
<p style="text-align:start">【新增】TinyMCE新增新年插件</p> 
<p style="text-align:start">【优化】利用ready为false时组件未渲染，对数据进行必要的预处理，更好的对后端数据类型容错。</p> 
<p style="text-align:start">【优化】第三方js库不在首页加载尽量都懒加载化处理</p> 
<p style="text-align:start">【修复】修复FormBuilder商品价格sku编辑类型</p> 
<p style="text-align:start">【修复】ListBuilder中筛选下拉框当前label显示</p> 
<p style="text-align:start">【新增】除了在左侧导航打开新页面外支持在ListBuilder弹窗打开远程组件</p> 
<p style="text-align:start">【修改】修改远程组件与iframe规范新增outUrl承载外部链接</p> 
<p style="text-align:start">【修复】修复前端接管数据预处理后导致的el-dialog无法打开</p> 
<p style="text-align:start">【变更】iframe和远程组件采用outUrl加载并且自动判断是否要补齐域名</p> 
<p style="text-align:start">【优化】优化在业务中比如表单提交完成自动关闭弹窗接口</p> 
<p style="text-align:start">【新增】远程组件支持传递query参数</p> 
<p style="text-align:start">【新增】支持远程自定义Form组件来满足系统内置组件不符合业务需要的场景</p> 
<p style="text-align:start">【新增】文件上传组件images/files支持多选</p> 
<p style="text-align:start">【修复】修复高德地图组件对默认值的解析</p> 
<p style="text-align:start">【优化】优化高德地图数据结构便于地图中心定位</p> 
<p style="text-align:start">【修复】修复表单提交成功有时无法自动刷新父页面数据</p> 
<p style="text-align:start">【修复】修复列表html类型不显示表头</p> 
<p style="text-align:start">【修复】修复InfoBuilder对options的解析</p> 
<p style="text-align:start">【新增】新增底部表单按钮文字自定义及显隐</p> 
<p style="text-align:start">【修复】修复表单联动受数据预处理影响</p> 
<p style="text-align:start">【新增】FormBuilder支持表单项目分组</p> 
<p style="text-align:start">【新增】FormBuilder新增分栏概念取代之前的position位置概念</p> 
<p style="text-align:start">【新增】ListBuilder新增单元格点击快速编辑功能</p> 
<p style="text-align:start">【新增】新增左边树导航，右边内容编辑的ColBuilder</p> 
<p style="text-align:start">【修复】修复时间区间选择formatDates方法</p> 
<p style="text-align:start">【新增】xy-mavon-editor支持blockquote背景色等语法</p> 
<p style="text-align:start">【修复】修复同步token导致不停登录失败</p> 
<p style="text-align:start">【修复】修复FormBuilder对日期中HH的解析</p> 
<p style="text-align:start">【修复】修复default-checked-keys导致tree组件父节点半选无法回显状态问题</p> 
<p style="text-align:start">【修复】修复按钮打开页面模式下提交成功未能自动关闭页面</p> 
<p style="text-align:start">【新增】支持扫码登录规范</p> 
<p style="text-align:start">【新增】左侧菜单支持只在开发模式显示</p> 
<p style="text-align:start">【修复】修复ListBuilder的tags类型</p> 
<p style="text-align:start">【新增】左侧导航支持展开高亮当前页面</p> 
<p style="text-align:start">【新增】列表顶部和右侧按钮支持外链</p> 
<p style="text-align:start">【新增】支持右上角工具栏自定义</p> 
<p style="text-align:start">【新增】支持自动将菜单树状结构转换成前端所需要的路由</p> 
<p style="text-align:start">【新增】列表任意栏都支持打开弹窗列表</p> 
<p style="text-align:start">【新增】列表新增id和multitext类型</p> 
<p style="text-align:start">【新增】表单支持单独指定提交接口地址</p> 
<p style="text-align:start">【新增】列表支持采用时间线形式展示数据</p> 
<p style="text-align:start">【新增】表单上传组件支持预览音频和视频</p> 
<p style="text-align:start">【新增】支持图形验证</p> 
<p style="text-align:start">【新增】支持自定义下拉菜单的功能</p> 
<p style="text-align:start">【新增】表单支持直接播放音视频</p>
                                        </div>
                                      
</div>
            