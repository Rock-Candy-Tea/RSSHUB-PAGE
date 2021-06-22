
---
title: 'Android 组件化'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada09a1f51aa442bbd024bd92c62c284~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 18:05:05 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada09a1f51aa442bbd024bd92c62c284~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1.组件化的优势
Android APP组件化架构的目标:告别结构臃肿，让各个业务变得相对独立，业务组件在组件模式下可以独立开发，而在集成模式下又可以变为arr包集成到“app壳工程”中，组成一个完整功能的APP；从组件化工程模型中可以看到，业务组件之间是独立的，没有关联的，这些业务组件在集成模式下是一个个library，被app壳工程所依赖，组成一个具有完整业务功能的APP应用，但是在组件开发模式下，业务组件又变成了一个个application，它们可以独立开发和调试，由于在组件开发模式下，业务组件们的代码量相比于完整的项目差了很远，因此在运行时可以显著减少编译时间。</p>
<p>2.组件化项目架构详解</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada09a1f51aa442bbd024bd92c62c284~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>左图是项目组件化工程模型</p>
<p>集成模式: 所有的业务组件被“app壳工程”依赖，组成一个完整的APP；</p>
<p>组件模式:   可以独立开发业务组件，每一个业务组件就是一个APP；</p>
<p>app壳工程: 负责管理各个业务组件，和打包apk，没有具体的业务功能；</p>
<p>业务组件: 根据公司具体业务而独立形成一个个的工程；</p>
<p>Main组件:属于业务组件，指定APP启动页面、主界面 ；</p>
<p>Common组件:   也就是功能组件(component_base 模块)，支撑业务组件的基础，提供多数业务组件需要的功能，例如提供网络请求功能；</p>
<p>component_data组件: 存放与项目相关的公共数据,例如bean的基类,IntentKV存数据的键值对等.</p>
<p>SDK组件: 集成微信,支付宝支付,分享,推送等常用的第三方框架.</p>
<p>3.项目中实践</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1ee1a8479d04a30815cf535414d67eb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3.1.kotlin+MVP+组件化对项目框架搭建</p>
<p>View：UI层，显示数据，并且向Presenter层报告用户行为</p>
<p>Model：数据层，负责与网络层、数据库层逻辑交互</p>
<p>Presenter：从Model拿数据应用到UI层管理UI状态，决定显示什么，响应用户行为</p>
<p>3.2组件化划分详情</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbe22734fec44465b7a204338dec19f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
3.3项目目录划分</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7e7a0d2dbaf4ad9ba4773b0afc78912~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
4.组件化搭建流程
4.1组件模式和集成模式切换的实现:
4.1.1 config.gradle文件增加变量配置
ext &#123;</p>
<pre><code class="copyable">isMineApplication = false  //HomeModule开关，false:作为Lib组件存在， true:作为application存在
isHomeApplication = false  //MineModule开关，false:作为Lib组件存在， true:作为application存在
isMessageApplication = false //MessageModule开关，false:作为Lib组件存在， true:作为application存在
isPrepareLessonApplication = false // PrepareLessonModule开关，false作为Lib组件存在，true：作为application存在
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
4.1.2组件模式和集成模式切换的实现（每个业务模块gradle配置如下）:
if (rootProject.ext.isPrepareLessonApplication) &#123;
apply plugin: 'com.android.application'
&#125; else &#123;
apply plugin: 'com.android.library'
&#125;
4.1.3组件之间AndroidManifest合并：
在 Android中每一个组件都会有对应的 AndroidManifest.xml，用于声明需要的权限、Application、Activity、Service、Broadcast等，当项目处于组件模式时，业务组件的 AndroidManifest.xml 应该具有一个 Android APP 所具有的的所有属性，尤其是声明 Application 和要 launch的Activity，但是当项目处于集成模式的时候, 我们要为组件开发模式下的业务组件再创建一个AndroidManifest.xml，然后根据isModule指定AndroidManifest.xml的文件路径，让业务组件在集成模式和组件模式下使用不同的AndroidManifest.xml。</p>
<p>sourceSets &#123;
main &#123;
if (rootProject.ext.isPrepareLessonApplication) &#123;
manifest.srcFile 'src/main/module/AndroidManifest.xml'
&#125; else &#123;
manifest.srcFile 'src/main/AndroidManifest.xml'
&#125;
jniLibs.srcDirs = ['libs']
&#125;
&#125;
4.1.4单独业务组件Application独立初始化问题：
当部分模块有特有功能时候，有些初始化操作需要在某个模块的Application的onCreate中做初始化操作：</p>
<p>此处举例我们项目中的个人中心模块（MineMoudle）需要单独对智齿sdk做初始化操作我们不可能写在Library的BaseApplication去做初始化操作，如果在BaseApplication中去做初始化操作当我们打包其中某一个业务模块时（不使用智齿sdk的业务的模块）此时的BaseApplication如果做初始化智齿sdk的操作是不合理的。解决方案如下：</p>
<p>在BaseApplication的onCreate方法中调用如下方法（反射+多态思想实现单独模块的初始化方法调用）：</p>
<p>/**</p>
<ul>
<li>初始化各个Module单独需要在Application中初始化的业务</li>
<li>每个组件的BaseApplicationImp都需要将绝对</li>
<li>路径存储到ModuleConfig.MODULELIST中以便通过反射初始化</li>
<li>进而调用onCreate进行单独module的初始化</li>
</ul>
<p>*/
private fun initModuleConfig() &#123;
ModuleConfig.MODULE_PATH_LIST.forEach &#123; moduleImpl ->
try &#123;
val clazz = Class.forName(moduleImpl)
val obj = clazz.newInstance()
if (obj is BaseApplicationImp) &#123;
obj.onCreate(this)
&#125;
&#125; catch (e: ClassNotFoundException) &#123;
e.printStackTrace()
&#125; catch (e: IllegalAccessException) &#123;
e.printStackTrace()
&#125; catch (e: Fragment.InstantiationException) &#123;
e.printStackTrace()
&#125;
&#125;
&#125;
ModuleConfig.MODULE_PATH_LIST 配置如下
interface ModuleConfig &#123;
companion object &#123;
val MODULE_APP = "com.tal.firstleap.app.AppImp"
val MODULE_MINE = "com.tal.minemodule.app.MineModuleAppImp"
val MODULE_HOME = "com.tal.homemodule.app.HomeModuleAppImp"</p>
<pre><code class="copyable">    val MODULE_PATH_LIST = arrayOf(MODULE_APP,MODULE_MINE, MODULE_HOME)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
其中的MODULE_PATH_LIST常量存储的是在某个module重的BaseApplicationImp接口实现类的绝对路径</p>
<p>interface BaseApplicationImp &#123;
fun onCreate(application:Application)
&#125;</p>
<p>MineModuleAppImp存在于某一个需要的业务组件
class MineModuleAppImp : BaseApplicationImp &#123;</p>
<pre><code class="copyable">//做此Module的Application中需要初始化的业务
override fun onCreate(application: Application) &#123;
    //参数3 用户的唯一标识，不能传一样的值，可以为空
    SobotApi.initSobotSDK(application, Constant.SABOT_APP_KEY,"")
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
4.1.5组件间通信
使用了阿里Arouter实现页面跳转以及数据传递，详情如下
<a href="https://github.com/alibaba/ARouter" target="_blank" rel="nofollow noopener noreferrer">github.com/alibaba/ARo…</a></p></div>  
</div>
            