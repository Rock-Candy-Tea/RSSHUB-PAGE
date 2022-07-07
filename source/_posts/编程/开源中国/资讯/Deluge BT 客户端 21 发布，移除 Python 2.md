
---
title: 'Deluge BT 客户端 2.1 发布，移除 Python 2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2938'
author: 开源中国
comments: false
date: Thu, 07 Jul 2022 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2938'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Deluge 是一个功能齐全的 BitTorrent 客户端，具有 GTK、Web UI 和命令行界面。它以 libtorrent 为核心来处理 BitTorrent 协议。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">近日 Deluge 2.1 正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">主要变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>取消对 Python 2 的支持（Python >= 3.6）</li> 
 <li>libtorrent 的最低要求提高（>=1.2）</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Core</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>增加对 SVG 跟踪器图标的支持</li> 
 <li>修复跟踪器图标的错误处理</li> 
 <li>修复清理跟踪器图标临时文件</li> 
 <li>修复插件管理器以处理新的元数据 2.1</li> 
 <li>隐藏配置日志中的密码</li> 
 <li>修复清理 add_torrent_url 中的临时文件。</li> 
 <li>修复 torrent 删除后 sessionproxy 中的 KeyError</li> 
 <li>移除 libtorrent 的废弃函数</li> 
 <li>修复 file_completed_alert 处理</li> 
 <li>增加对 pygeoip 依赖关系的支持</li> 
 <li>修复对 Windows 保护文件夹的崩溃记录</li> 
 <li>增加 is_interface 和 is_interface_name 来验证网络接口</li> 
 <li>在 host 列表中增加对 IPv6 的支持</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Web UI</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 ETA 列排序顺序</li> 
 <li>修复了定义前景和背景颜色的问题</li> 
 <li>接受 json 消息的内容类型中的字符集</li> 
 <li>修正对 torrent 属性的 HTML 实体的编码，以防止 XSS。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Gtk UI</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复下载位置文本框宽度</li> 
 <li>修复连接管理器中隐藏的端口号</li> 
 <li>增加连接管理器默认高度</li> 
 <li>使用 ico 或 gif 图标为 Windows 上的崩溃添加解决方法</li> 
 <li>在日志中隐藏帐户密码长度</li> 
 <li>测试开放端口时使用 GtkSpinner</li> 
 <li>修复 ETA 被复制到相邻的空单元格</li> 
 <li>在 Windows 上默认禁用 GTK CSD</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeluge.readthedocs.io%2Fen%2Flatest%2Fchangelog.html" target="_blank">https://deluge.readthedocs.io/en/latest/changelog.html</a></p>
                                        </div>
                                      
</div>
            