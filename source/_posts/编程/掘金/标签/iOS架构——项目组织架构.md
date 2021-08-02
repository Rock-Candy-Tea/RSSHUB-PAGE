
---
title: 'iOS架构——项目组织架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4360'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:50:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=4360'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>关键字：项目组织架构 CocoaPod + 多项目级联 + xib + MVVM<br>
整体项目结构：</p>
<pre><code class="copyable">ProjectApp   项目app project
    Vendors    第三方.a、.framework库或源码
    Resources  项目静态配置文件
    Database    数据库文件夹，如CoreData
    Component  此项目特定的组件
        Base    此项目特定的基类，此基类基本上都要集成ComponentUI里的Base，如BaseNavController, BaseVC, BaseTabBarController
        Util    此项目特定的工具类
        UI    此项目特定的UI
    Common    此项目特定的公共类
        View   视图
        WebVC  公用的WebViewVC，需要提供接口出来，不建议直接调用
        Pay   支付，如微信、支付宝支付
        Push  推送，如极光、友盟
        DataCache  项目数据缓存，如图片缓存类
        BugAnalysis   app闪退奔溃统计
        DataStatistic   用户数据行为埋点统计，如友盟、极光的数据统计
        Map 高德、百度地图
        Bluetooth 蓝牙
        Wifi Wi-Fi
        Styles   整体风格，存放颜色、字体、边距
        CommonImport.swift   导入常用的库，这样就不用每次用的时候都需要导入了
    Service   封装所有接口
    Modules   项目模块
        Home   首页模块
           VC   存放VC、xib
           Model   业务逻辑
           View   视图
           Entity   普工实体模型，即POJO
        Mine  我的模块
        Main  主模块
        Login  登录模块
    Assets.xcassets  切图
        AccentColor
        AppIcon
Pods
    Podfile
ComponentNetwork  对第三方网络库对封装，如Alamofire
    AFService
    CPService.swift
ComponentUI    通用常用UI库的封装
    Base
    AlertView
ComponentUitls  通用常用工具类库
    App
    Array
    Color
    Date
    Device
    File
    Image
    Json
    Lanuage
    Object
    Path
    String
    Validate
    View
<span class="copy-code-btn">复制代码</span></code></pre>
<p>storyboard、xib的取舍<br>
不采用单个或多个Storyboard，采用一个VC对应一个XIB方式，如果只需要适配iOS 13以后，可以直接使用swiftUI。storyboard很臃肿，而且打开特别慢，页面视图多了后很难查找，每次创建VC都需要通过storyboard，不够简明，团队编写极易代码冲突。也不建议界面UI实现都采用代码编写，纯代码编写效率低，维护困难，布局麻烦，代码量多。当然纯代码布局性能有提高，毕竟加载xib或storyboard需要消耗一定资源。</p>
<p>代码封装</p>
<ol>
<li>base类，主要分类三类</li>
</ol>
<ul>
<li>所有项目都通用都base，放到ComponentUI库base文件夹，主要封装一些打印信息、常用VC、View、UILabel、UIImage等功能</li>
<li>本项目特定的base，继承ComponentUI库base，定制项目通用的base，如通用导航栏navigationBar、tableView下拉刷新上拉加载更多等</li>
<li>某些页面共性封装，如同类产品详情页面、同类列表页面等</li>
</ul>
<ol start="2">
<li>建议所有第三方库都需要再封装一层</li>
</ol>
<ul>
<li>iOS编程语言、系统更新都很快，第三方库不一定能及时更行</li>
<li>随着项目的扩张，某些第三方库已经无法满足需求，需要找替代品</li>
<li>第三方库功能过多，需要封装出项目特定的API接口</li>
</ul>
<ol start="3">
<li>Assets.xcassets切图<br>
一般每个模块创建一个文件夹，然后再增加一个Common公共文件夹，尽可能切成等比例方形，某些特定场合才切成不等比图片，命名规则：统一命名成英文小写，多个单词间由下划线_分隔,同一项目不能出现同名切图，格式：模块名/页面名+功能名+状态名，如登陆页面的密码眼睛名称为login_account_enable.png，有条件的团队可以统一全部使用矢量图，如IconFont等</li>
<li>架构适用性<br>
此接口适合中型app项目，小型项目可以把ComponentNetwork、ComponentUI、ComponentUtils移植到ProjectApp的Component下，直接一个项目project+Pods就可以。大型项目的话可以把ProjecctApp里Modules下每个模块单独作为一个project，Common、Service、Database、Vendor各作为一个project，然后ProjectApp依赖各个project模块。如果需要对外提供SDK的同样需要再抽离出project。</li>
<li>架构分层<br>
不要被MVC、MVVM、VIPER等架构锁死，这些架构只是提供一些思路，学会了需要灵活运用，总结归纳，适合自己的才是最好的</li>
</ol>
<p>项目源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodechina.csdn.net%2Fios1%2Fprojectapp" target="_blank" rel="nofollow noopener noreferrer" title="https://codechina.csdn.net/ios1/projectapp" ref="nofollow noopener noreferrer">codechina.csdn.net/ios1/projec…</a></p>
<h4 data-id="heading-0"><a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fdocs.qq.com%252Fdoc%252FDUnZ0R1d6QUVCWU1W" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDUnZ0R1d6QUVCWU1W" ref="nofollow noopener noreferrer">相关面试资料</a></h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F4212bc62699d" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/4212bc62699d" ref="nofollow noopener noreferrer">收录</a></p></div>  
</div>
            