
---
title: '一体机支持使用硬件设备国密加密，JumpServer 堡垒机 v2.26.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/1fa659a1475848f5882b6d8e4880c65e~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=2QOgirsLRXCGM%2By2e5BSgZnSNhU%3D'
author: 开源中国
comments: false
date: Mon, 19 Sep 2022 13:19:00 GMT
thumbnail: 'https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/1fa659a1475848f5882b6d8e4880c65e~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=2QOgirsLRXCGM%2By2e5BSgZnSNhU%3D'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/1fa659a1475848f5882b6d8e4880c65e~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=2QOgirsLRXCGM%2By2e5BSgZnSNhU%3D" referrerpolicy="no-referrer"> 
 <p style="margin-left:0px; margin-right:0px">2022年9月19日，JumpServer开源堡垒机正式发布v2.26.0版本。基于该版本的JumpServer一体机支持使用硬件设备的国密加密。认证方面，新版本的JumpServer支持用户自定义认证逻辑，满足了一部分企业用户使用独特认证方式的需求。另外，在数据库代理连接方面（KoKo组件），新增支持MongoDB SSL/TLS以及Redis SSL/TLS的连接。</p> 
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">X-Pack增强包方面，针对短信服务，JumpServer除了支持腾讯云、阿里云和CMPP v2.0协议以外，这一版本还新增支持华为云短信服务。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">同时，在“云同步”模块中，JumpServer新增支持腾讯云轻量应用服务器（TencentCloud Lighthouse）以及天翼云私有云同步。此前，JumpServer在多云资产纳管方面已经实现了对阿里云、腾讯云、华为云、百度云、京东云、AWS（中国）、AWS（国际）、Azure（中国）、Azure（国际）、谷歌云、VMware、青云私有云、华为私有云、OpenStack、Nutanix、Fusion Compute、局域网的支持，有效协助用户实现对私有云、公有云资产的统一纳管。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">此外，在改密计划模块中，JumpServer新增支持MongoDB数据库改密（暂不支持MongoDB SSL/TLS改密），满足了用户对数据库密码的相关安全策略要求。目前已支持改密的数据库类型包括：MySQL、MariaDB、Oracle、PostgreSQL、SQL Server和MongoDB。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">新增功能</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">1. JumpServer一体机支持使用硬件设备的国密加密</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">基于JumpServer v2.26.0版本的JumpServer一体机支持使用硬件设备的国密加密。国密算法是国家密码管理局制定的自主可控的国产算法，实现了数据的安全传输。为了保证数据的安全传输，JumpServer一体机新增支持使用硬件设备的国密加密。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">2. 支持用户自定义认证逻辑</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在JumpServer v2.26.0版本中，支持用户自定义认证逻辑。目前JumpServer已经支持的认证方式虽然众多，但是有一部分企业仍会采用自己独特的认证方式，这些认证方式不在业界标准之内。针对这一现实场景，JumpServer开放出一个标准接口来实现这个功能。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">如果企业想在JumpServer服务中对接自己独特的认证方式，可以按照以下配置流程进行操作：</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">① 在<em>/opt/jumpserver/core/data</em>目录下创建一个auth目录，其中包含两个文件:</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">■ __init__.py；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left">■ main.py；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">② __init__.py文件中不需要填写任何内容；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">③ 在main.py文件中确定一个authentication方法（参考下面的main.py文件，认证的逻辑一般由用户方实现）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">④ 在config.txt配置文件中，配置<em>AUTH_CUSTOM=true</em>；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">⑤在config.txt配置文件中，配置<em>AUTH_CUSTOM_FILE_MD5=&#123;main.py文件的md5值&#125;</em>；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">⑥ 配置完成后，重启JumpServer服务。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>注意事项：</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">■ 按照配置流程配置完成后启动服务，再修改<br> <em><span>/opt/jumpserver/core/data/auth/main.py</span></em>文件，新的认证逻辑不会生效，需要再次更新<em>AUTH_CUSTOM_FILE_MD5</em>的值并重启服务（从安全考虑角度），新的认证逻辑才会生效；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">■ 只有<em>AUTH_CUSTOM=true</em>，并且<em>AUTH_CUSTOM_FILE_MD5</em>值正确的情况下，自定义认证方式才会被启用。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong>main.py文件代码示例：</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#00753b">""" Customize the authentication module """</span>
  
  
<span style="color:#8a7304"><span style="color:#114ba6">def</span> <span style="color:#a82e2e">authenticate</span><span>(username, password, **kwargs)</span>:</span>
    <span style="color:#00753b">""" Customize the authentication method
  
    :param username: Login user username
    :param password: Login user password
    :param kwargs: Login user other auth-info
  
    :returns:
        The return value type is dict.
        The return value must contain fields: `name`(str),`username`(str),`email`(str),
        Optional fields: `is_active`(bool)
  
        demo:
        &#123;
          'name': 'JumpServer',
          'username': 'jumpserver',
          'email': 'jumpserver@fit2cloud.com',
          'is_active': True
        &#125;
    """</span>
    <span style="color:#114ba6">return</span> &#123;
        <span style="color:#00753b">'name'</span>: <span style="color:#00753b">'JumpServer'</span>,
        <span style="color:#00753b">'username'</span>: <span style="color:#00753b">'jumpserver'</span>,
        <span style="color:#00753b">'email'</span>: <span style="color:#00753b">'jumpserver@fit2cloud.com'</span>,
        <span style="color:#00753b">'is_active'</span>: <span style="color:#8a7304">True</span>
    &#125;</code></pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">3. KoKo组件支持MongoDB SSL/TLS、Redis SSL/TLS连接</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在JumpServer v2.26.0版本中，数据库代理连接（KoKo组件）新增支持MongoDB SSL/TLS以及Redis SSL/TLS的连接。管理员通过选择“应用管理”→“数据库”，创建“MongoDB”或“Redis”数据库，在创建表单上启用SSL/TLS，并上传证书。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/4cf17e981ab640519ab7c1edde8d4bdf~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=9GrK%2Fuox7B2w8gHAZF1%2BI5reSsw%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">            ▲ 图1 创建MongoDB或Redis数据库，开启SSL/TLS，并上传证书</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/a03e7139097a4f4088f7bb2b2ab8fed4~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=bQuPohPsL4IY213S%2B0zLrf%2BSVpI%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">                         ▲ 图2 测试连接MongoDB SSL/TLS，连接成功</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/e3e3afae0d3d43e7aa77ba63356eba1a~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=Zo3HEktvfH2lp%2BYaKdwCp4A5dVc%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">                            ▲ 图3 测试连接Redis SSL/TLS，连接成功</span>
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">4. 短信服务支持华为云短信平台（X-Pack增强包内）</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在JumpServer v2.26.0版本中，短信服务在腾讯云、阿里云和CMPP v2.0协议的基础上，新增支持华为云短信平台。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">管理员选择“系统设置”→“短信设置”，选择“华为云”选项进行配置，并且启用SMS。用户在“个人信息”页面中，开启多因子（MFA）认证，同时启用短信认证。此后，用户在二次认证登录时，即可使用华为云短信服务进行短信验证码认证。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/02180d0b681f4e2f90fcd20e38b94ba1~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=w8qkehHqPTh28%2B1rZp0rGqDTqyo%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">                         ▲ 图4 华为云短信服务配置（X-Pack增强包内）</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/d01db5ceb182487680d95066cc1163ce~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=DqLEPDlWnuKYH3mVy6qLNccFetc%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲ 图5 用户在进行二次认证登录时，即可使用华为云短信服务进行短信验证码认证</span>
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">5. 云同步支持腾讯云轻量应用服务器以及天翼云私有云同步（X-Pack增强包内）</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在JumpServer v2.26.0版本中的“云同步”模块中，新增支持腾讯云轻量应用服务器（TencentCloud Lighthouse）以及天翼云私有云同步。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">此前，JumpServer在多云资产纳管方面已经实现了对阿里云、腾讯云、华为云、百度云、京东云、AWS（中国）、AWS（国际）、Azure（中国）、Azure（国际）、谷歌云、VMware、青云私有云、华为私有云、OpenStack、Nutanix、Fusion Compute、局域网的支持，有效协助用户实现对私有云、公有云资产的统一纳管。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">管理员通过选择“资产列表”→“云同步”，创建“腾讯云（轻量应用服务器）”或“天翼云”账号，并创建同步任务，即可将符合IP规则的云资产同步到JumpServer进行统一纳管。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/0d96d6aed564439ab0d145bda5b2ed9a~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=OyJk0rkRw4CkfWJxLY72OGoIWgw%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲ 图6 通过“资产列表”→“云同步”，创建“腾讯云（轻量应用服务器）”账号</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/2915b751d74e4384acd27e6258f73db3~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=maU6%2B0IoPPSHhlJaE5u2K9LVCio%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">                           ▲ 图7 创建腾讯云轻量应用服务器同步任务</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/636e8a31b5564125b0d847740161ca43~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=tmDpWmex4vXoNmL4UbymyOy%2FBHE%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲ 图8 同步成功后，在资产列表页面可查看同步过来的腾讯云轻量应用服务器资产</span>
</div> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#279a81">6. 改密计划新增支持MongoDB数据库改密（X-Pack增强包内）</span></strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">在“改密计划”模块中，JumpServer新增支持MongoDB数据库改密（暂不支持MongoDB SSL改密），满足了用户对数据库密码的相关安全策略要求。</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify">目前JumpServer已支持改密的数据库类型包括：MySQL、MariaDB、Oracle、PostgreSQL、SQL Server以及MongoDB。同时，在创建应用改密计划时，JumpServer提供了三种密码策略供管理员进行选择。</p> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/813b89e56bf849278639c1489b5d3151~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=WWgrVDE7grA%2BmYrSFtBHrK3Ma7c%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲ 图9 选择“账号管理”→“改密计划”进行应用改密，创建MongoDB改密计划</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/72dc65befdff4460acca87398c44f98c~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=pmVarmeJeEV0KbnlsXD%2FYQY8G5M%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲图10 待改密计划任务触发后，在应用改密计划列表页面即可查看其执行次数</span>
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <img src="https://p3-sign.toutiaoimg.com/tos-cn-i-qvj2lq49k0/bf6204acae16458688c41f495cd6fef7~noop.image?_iz=58558&from=article.pc_detail&x-expires=1664168225&x-signature=1nGe62GhOks24UvutiPpTMSVJIg%3D" referrerpolicy="no-referrer">
</div> 
<div style="margin-left:0; margin-right:0; text-align:justify">
 <span style="color:#999999">▲图11 在“改密计划详情”页面执行列表Tab中可查看改密任务执行详细日志</span>
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">功能优化</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>优化对OAuth 2.0认证协议的自定义注销功能；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>优化系统工具Ping或Telnet输出结果使用UTF-8编码；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>第三⽅⽤户登录时，支持⽤户登录规则；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>优化Web Terminal页面，点击Logo跳转至主界面；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■<span> </span></span>优化Luna页面，重连资产时不刷新整个页面；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>优化账号备份的执行速度（X-Pack增强包内）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■<span> </span></span>优化工单列表的搜索过滤字段（X-Pack增强包内）；</p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span style="color:#279a81">■</span><span> </span>通过Web GUI方式连接PostgreSQL数据库时，支持自定义编码（X-Pack增强包内）。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:justify">Bug修复</h1> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复在线会话监控页面中布局部分被遮挡的问题；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复前端加密导致页面表单提交时偶尔报错的问题；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复批量更新资产时，页面加载速度慢的问题；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■<span> </span></span>修复配置MFA失效时间设置不生效的问题；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复设置了命令规则后，连接资产复制/粘贴多行命令执行时不能阻断的问题（KoKo组件）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复数据库命令过滤导致会话连接断开的问题（Magnus组件）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复服务长时间运行时会出现内存泄漏的问题（Magnus组件）；</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:justify"><span><span style="color:#279a81">■<span> </span></span>修复通过Windows 2008 R2连接资产时，不能录像的问题（Razor组件，X-Pack增强包内）；</span></p> 
<p style="color:#222222; margin-left:0px; margin-right:0px; text-align:justify"><span><span style="color:#279a81">■</span><span> </span>修复通过Linux XRDP连接资产时，没有录像和服务停止的问题（Razor组件，X-Pack增强包内）。</span></p>
                                        </div>
                                      
</div>
            