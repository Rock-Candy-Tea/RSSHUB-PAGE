
---
title: '嘿 Siri，唤醒电脑'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/06/18/33bab3b5f4f7807c65014021f1e12c99.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Fri, 18 Jun 2021 04:48:02 GMT
thumbnail: 'https://cdn.sspai.com/2021/06/18/33bab3b5f4f7807c65014021f1e12c99.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-e1f0100a><div class="content wangEditor-txt minHeight" data-v-e1f0100a><blockquote><p>没有Siri的iOS不是一个好OS</p></blockquote><p>之前提到 关于<a href="https://sspai.com/post/67003">网络唤醒WoL</a> 这块的内容，也列举了很多唤醒工具，目的是为更好地对远端计算机进行有效的管控，这次更进一步，解放双手，尝试让「语音助手」执行唤醒操作。</p><h2>构思</h2><p>原理亦不复杂，笔者手头有台ipad Air：「Siri」充当 语音助手，调用「捷径」发送指令。</p><p>因「捷径」本身不支持WoL协议，但能发起HTTP请求，因此我们需要一个能让不同协议进行沟通/转换的装置/程序，我们简称「协议转换器」，处理HTTP请求并发送WoL唤醒信号。</p><p>我们知道有 <a href="https://www.home-assistant.io/"><u>Home Assistant</u></a> 这类平台专门用于构建智能家居交互核心，但对于单一简单需求来说，未免显得过于笨重，所以我决定自己实现一个。如果你已经部署某些类似的物联网核心，可以尝试对其进行扩展或集成。</p><p>总流程如下：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/33bab3b5f4f7807c65014021f1e12c99.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/33bab3b5f4f7807c65014021f1e12c99.png" referrerpolicy="no-referrer"></figure><ul><li>本地局域网已有一台树莓派2，作为程序运行的载体</li><li>HTTP 与 WoL 同属网络协议，在此我们使用 <strong>Golang </strong>来构建上图的两大功能模块</li><li>HTTP请求 先不设计得非常复杂，够用就行<sup class="ss-footnote" href title="「过早优化是万恶之源」—— 高德纳" footnote-id="1">1</sup><code>http://192.168.1.4:40080/wakeup</code></li><li>得益于HTTP协议的泛用性，亦可以通过各种浏览器方便地调用，唤醒远程计算机</li></ul><h2>试验</h2><h3>iOS</h3><p>新建捷径 > 获取URL内容 > HTTP GET 方法</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/3158e28b81b7e3b1b9958fb869fcb515.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/3158e28b81b7e3b1b9958fb869fcb515.png" referrerpolicy="no-referrer"></figure><p>开启「互联网、麦克风及语音识别」</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/cf46a869132261702021fcadd0b8d3d2.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/cf46a869132261702021fcadd0b8d3d2.png" referrerpolicy="no-referrer"></figure><p>嘿Siri，「快捷指令名称」</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/18/21deb4a54ac99a72cb6f94cecbe6621e.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/18/21deb4a54ac99a72cb6f94cecbe6621e.png" referrerpolicy="no-referrer"></figure><p>捷径名称可任意发挥，喊得顺就行</p><h3>协议转换器</h3><p>程序入口 main.go</p><pre class="language-null"><code>package main

import (
"encoding/json"
"fmt"
"log"
"net/http"
)

func handler_status(w http.ResponseWriter, r *http.Request) &#123;
fmt.Fprintf(w, "0")
&#125;

func handler_wakeup(w http.ResponseWriter, r *http.Request) &#123;
sendwol()
fmt.Fprintf(w, "0")
&#125;

func main() &#123;
http.HandleFunc("/", handler)

// Service Status Check
http.HandleFunc("/status", handler_status)

// WOL
http.HandleFunc("/wakeup", handler_wakeup)

// HTTP
err := http.ListenAndServe(":8000", nil)
log.Fatal(err)
&#125;</code></pre><p>从 <a href="https://github.com/zzustu/wol/blob/master/main.go">GitHub </a>扒拉两个函数实现WoL协议包 wol.go</p><pre class="language-null"><code>package main

import (
"bytes"
"encoding/hex"
"errors"
"fmt"
"net"
)

func sendwol() &#123;
  // 目标MAC地址与指定网卡接口
const hw  = "e0db55a893e6"
const nic = "eth0"

macHex, err := hex.DecodeString(hw)
if err != nil &#123;
fmt.Printf("MAC: [%s] decode fail.\n", hw)
return
&#125;

// 广播MAC地址 FF:FF:FF:FF:FF:FF
var bcast = []byte&#123;0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF&#125;
var buff bytes.Buffer
buff.Write(bcast)
for i := 0; i < 16; i++ &#123;
buff.Write(macHex)
&#125;

// 获得唤醒魔包
mp := buff.Bytes()
if len(mp) != 102 &#123;
fmt.Printf("MAC: [%s] length too short.\n", hw)
return
&#125;

sendMagicPacket(mp, nic)
&#125;

// 向指定网卡发送唤醒魔包
func sendMagicPacket(mp []byte, nic string) &#123;
sender := net.UDPAddr&#123;&#125;
if len(nic) != 0 &#123;
ip, err := interfaceIPv4ByName(nic)
if err != nil &#123;
fmt.Printf("网卡[%s]错误: %s", nic, err)
return
&#125;

sender.IP = ip
&#125;

target := net.UDPAddr&#123;
IP: net.IPv4bcast,
&#125;
conn, err := net.DialUDP("udp", &sender, &target)
if err != nil &#123;
fmt.Printf("创建UDP错误：%v", err)
return
&#125;
defer func() &#123;
_ = conn.Close()
&#125;()

_, err = conn.Write(mp)
if err != nil &#123;
fmt.Printf("魔包发送失败[%s]", err)
&#125; else &#123;
fmt.Printf("魔包发送成功\n")
&#125;
&#125;

// 通过网卡名称获取该网卡绑定的IPv4
func interfaceIPv4ByName(nic string) (net.IP, error) &#123;
inter, err := net.InterfaceByName(nic)
if err != nil &#123;
return nil, err
&#125;

// 检查网卡是否正在工作
if (inter.Flags & net.FlagUp) == 0 &#123;
return nil, errors.New("网卡未工作")
&#125;

addrs, err := inter.Addrs()
if err != nil &#123;
return nil, err
&#125;

for _, addr := range addrs &#123;
if ip, ok := addr.(*net.IPNet); ok &#123;
if ipv4 := ip.IP.To4(); ipv4 != nil &#123;
return ipv4, nil
&#125;
&#125;
&#125;

return nil, errors.New("该网卡没有IPv4地址")
&#125;</code></pre><h3>安装Golang & 编译 & 试运行</h3><p><code>apt-get install golang && go run main.go wol.go</code></p><h2>正式环境</h2><h3>程序托管</h3><p>为了保证程序长时间稳定运行，请个「保姆」，由 <strong>Systemd </strong>对「协议转换器」进行托管</p><p><code>vim /etc/systemd/system/assist.service</code></p><pre class="language-shell"><code>[Unit]
Description = Assistant Service
[Service]
ExecStart = /usr/local/bin/assist
Restart = always
Type = simple

[Install]
WantedBy = multi-user.target</code></pre><h3>生成二进制文件 & 存放于合适位置</h3><p><code>go build main.go wol.go & cp main /usr/local/bin/assist</code></p><h3>启动</h3><p><code>systemctl daemon-reload & systemctl start assist</code></p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/06/17/d80380e334dea3012f336cdfea6a25bb.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/06/17/d80380e334dea3012f336cdfea6a25bb.png" referrerpolicy="no-referrer"></figure><p>后续还可在此基础上进行扩展，集成「miIO」协议，自由操控物联网设备</p><p>最后来看看效果</p><iframe class="ss-videoIframe" src="//player.bilibili.com/player.html?bvid=BV1jU4y1G7d1"> </iframe><h2>附</h2><p style="margin-left:auto;"><a href="https://support.apple.com/en-us/HT208280">Control your home with Siri</a></p><p style="margin-left:auto;"><a href="https://www.amd.com/system/files/TechDocs/20213.pdf">网络唤醒魔包技术白皮书</a></p></div><!----></div><div style="border:1px solid transparent;" data-v-e1f0100a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-e1f0100a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>5</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>2</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-971" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E5%98%BF%20Siri%EF%BC%8C%E5%94%A4%E9%86%92%E7%94%B5%E8%84%91%E3%80%91%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F06%2F18%2Fb16d4f2b4f1f6478f1cfa2ab56a1720d.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="icon icon-article_weibo right-16"></i></a><span><div role="tooltip" id="el-popover-2625" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><i class="icon icon-article_weixin right-16"></i></span><a href="https://twitter.com/share?text=%E3%80%90%E5%98%BF%20Siri%EF%BC%8C%E5%94%A4%E9%86%92%E7%94%B5%E8%84%91%E3%80%91%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="icon icon-article_twitter right-16"></i></a></div></div><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            