
---
title: '如何看待游戏《我的世界》（Minecraft）遭到大规模网络攻击？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic4.zhimg.com/v2-30c037cc924a522931bb68d1dc4b7131_1440w.jpg'
author: 知乎
comments: false
date: Sun, 12 Dec 2021 13:03:33 GMT
thumbnail: 'https://pic4.zhimg.com/v2-30c037cc924a522931bb68d1dc4b7131_1440w.jpg'
---

<div>   
Glavo的回答<br><br><h2>客户端</h2><p data-pid="y8gShSh1">HMCL 用户请尽快更新至最新开发版 3.4.212（设置>通用>启动器更新>测试版），3.4.212 以及更新版本的 HMCL 启动的 Minecraft 将不会遭受此漏洞的攻击。我们也在尽量努力解决剩下的少许其他残存问题，准备尽快发布新的正式版。</p><figure data-size="normal"><img src="https://pic4.zhimg.com/v2-30c037cc924a522931bb68d1dc4b7131_1440w.jpg" data-rawwidth="922" data-rawheight="604" data-size="normal" data-caption data-default-watermark-src="https://pic4.zhimg.com/v2-9cbb89d8e2867f02702f82e4bae8d0ed_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic4.zhimg.com/v2-30c037cc924a522931bb68d1dc4b7131_r.jpg" referrerpolicy="no-referrer"></figure><p data-pid="sJLd_3hJ">PCL 等其他启动器也尽快更新至最新版本，并且尽量重新安装已安装版本（Mojang 官方已修复，需要重新下载 <code>version.json</code> 和对应的 <code>client.xml</code>）。</p><h2>服务器</h2><p data-pid="Oi9D0IMR">对于 Minecraft 服务器。如果您在使用 1.17 或更高版本，请设置 JVM 参数 <code>-Dlog4j2.formatMsgNoLookups=true</code>，以及环境变量 <code>LOG4J_FORMAT_MSG_NO_LOOKUPS=true</code> 。</p><p data-pid="3Op1YHwq">对于所有受影响版本（1.7 以及更高版本），请覆盖服务器 log4j 配置。</p><p data-pid="Y898LkUe">具体是，对于 Minecraft 1.12 以及更高版本，请将这段内容保存为 <code>log4j2.xml</code>:</p><div class="highlight"><pre><code class="language-xml"><span><span class="cp"><?xml version="1.0" encoding="UTF-8"?></span>
<span class="nt"><Configuration</span> <span class="na">status=</span><span class="s">"WARN"</span> <span class="na">packages=</span><span class="s">"com.mojang.util"</span><span class="nt">></span>
    <span class="nt"><Appenders></span>
        <span class="nt"><Console</span> <span class="na">name=</span><span class="s">"SysOut"</span> <span class="na">target=</span><span class="s">"SYSTEM_OUT"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125;] [%t/%level]: %msg&#123;nolookups&#125;%n"</span> <span class="nt">/></span>
        <span class="nt"></Console></span>
        <span class="nt"><Queue</span> <span class="na">name=</span><span class="s">"ServerGuiConsole"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125; %level]: %msg&#123;nolookups&#125;%n"</span> <span class="nt">/></span>
        <span class="nt"></Queue></span>
        <span class="nt"><RollingRandomAccessFile</span> <span class="na">name=</span><span class="s">"File"</span> <span class="na">fileName=</span><span class="s">"logs/latest.log"</span> <span class="na">filePattern=</span><span class="s">"logs/%d&#123;yyyy-MM-dd&#125;-%i.log.gz"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125;] [%t/%level]: %msg&#123;nolookups&#125;%n"</span> <span class="nt">/></span>
            <span class="nt"><Policies></span>
                <span class="nt"><TimeBasedTriggeringPolicy</span> <span class="nt">/></span>
                <span class="nt"><OnStartupTriggeringPolicy</span> <span class="nt">/></span>
            <span class="nt"></Policies></span>
        <span class="nt"></RollingRandomAccessFile></span>
    <span class="nt"></Appenders></span>
    <span class="nt"><Loggers></span>
        <span class="nt"><Root</span> <span class="na">level=</span><span class="s">"info"</span><span class="nt">></span>
            <span class="nt"><filters></span>
                <span class="nt"><MarkerFilter</span> <span class="na">marker=</span><span class="s">"NETWORK_PACKETS"</span> <span class="na">onMatch=</span><span class="s">"DENY"</span> <span class="na">onMismatch=</span><span class="s">"NEUTRAL"</span> <span class="nt">/></span>
            <span class="nt"></filters></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"SysOut"</span><span class="nt">/></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"File"</span><span class="nt">/></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"ServerGuiConsole"</span><span class="nt">/></span>
        <span class="nt"></Root></span>
    <span class="nt"></Loggers></span>
<span class="nt"></Configuration></span>
</span></code></pre></div><p data-pid="slG9LI38">对于 Minecraft 1.7~1.11.2，请将这段内容保存为 <code>log4j2.xml</code>:</p><div class="highlight"><pre><code class="language-xml"><span><span class="cp"><?xml version="1.0" encoding="UTF-8"?></span>
<span class="nt"><Configuration</span> <span class="na">status=</span><span class="s">"WARN"</span> <span class="na">packages=</span><span class="s">"net.minecraft,com.mojang"</span><span class="nt">></span>
    <span class="nt"><Appenders></span>
        <span class="nt"><Console</span> <span class="na">name=</span><span class="s">"SysOut"</span> <span class="na">target=</span><span class="s">"SYSTEM_OUT"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125;] [%t/%level]: %msg%n"</span> <span class="nt">/></span>
        <span class="nt"></Console></span>
        <span class="nt"><Queue</span> <span class="na">name=</span><span class="s">"ServerGuiConsole"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125; %level]: %msg%n"</span> <span class="nt">/></span>
        <span class="nt"></Queue></span>
        <span class="nt"><RollingRandomAccessFile</span> <span class="na">name=</span><span class="s">"File"</span> <span class="na">fileName=</span><span class="s">"logs/latest.log"</span> <span class="na">filePattern=</span><span class="s">"logs/%d&#123;yyyy-MM-dd&#125;-%i.log.gz"</span><span class="nt">></span>
            <span class="nt"><PatternLayout</span> <span class="na">pattern=</span><span class="s">"[%d&#123;HH:mm:ss&#125;] [%t/%level]: %msg%n"</span> <span class="nt">/></span>
            <span class="nt"><Policies></span>
                <span class="nt"><TimeBasedTriggeringPolicy</span> <span class="nt">/></span>
                <span class="nt"><OnStartupTriggeringPolicy</span> <span class="nt">/></span>
            <span class="nt"></Policies></span>
        <span class="nt"></RollingRandomAccessFile></span>
    <span class="nt"></Appenders></span>
    <span class="nt"><Loggers></span>
        <span class="nt"><Root</span> <span class="na">level=</span><span class="s">"info"</span><span class="nt">></span>
            <span class="nt"><filters></span>
                <span class="nt"><MarkerFilter</span> <span class="na">marker=</span><span class="s">"NETWORK_PACKETS"</span> <span class="na">onMatch=</span><span class="s">"DENY"</span> <span class="na">onMismatch=</span><span class="s">"NEUTRAL"</span> <span class="nt">/></span>
                <span class="nt"><RegexFilter</span> <span class="na">regex=</span><span class="s">".*\$\&#123;[^&#125;]*\&#125;.*"</span> <span class="na">onMatch=</span><span class="s">"DENY"</span> <span class="na">onMismatch=</span><span class="s">"NEUTRAL"</span><span class="nt">/></span>
            <span class="nt"></filters></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"SysOut"</span><span class="nt">/></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"File"</span><span class="nt">/></span>
            <span class="nt"><AppenderRef</span> <span class="na">ref=</span><span class="s">"ServerGuiConsole"</span><span class="nt">/></span>
        <span class="nt"></Root></span>
    <span class="nt"></Loggers></span>
<span class="nt"></Configuration></span>
</span></code></pre></div><p data-pid="AFFCIM0U">把 <code>log4j2.xml</code> 放到服务器 jar 旁，并添加 JVM 参数 <code>-Dlog4j.configurationFile=./log4j2.xml</code>。</p>  
</div>
            