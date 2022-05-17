
---
title: 'Archttp 0.1.0 发布更新，像 ExpressJS 真简单！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9560'
author: 开源中国
comments: false
date: Tue, 17 May 2022 22:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9560'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <p>Archttp 是 DLang 编写的轻量级框架，性能比肩 Fasthttp 等，但是语法清晰明了，这次调整也更倾向于轻量化设计的 ExpressJS，十分优雅，开发体验可以用优秀表达。</p> 
 <h3>整体 API 简化</h3> 
 <p>现在回调方法直接返回 request 和 response 而不是之前那样返回 context，更易于使用，启动过程也把 Bind() 和 Run() 合并为 Listen() 了，让开发者的代码少写一行是一样！</p> 
 <pre><code class="language-cs">
import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.Get("/", (request, response) &#123;
        response.send("Hello, World!");
    &#125;);

    app.Listen(8080);
&#125;
</code></pre> 
 <h3>支持 Cookie 写入</h3> 
 <pre><code class="language-cs">
import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.Get("/cookie", (request, response) &#123;
        response.cookie("username", "myuser");
        response.cookie(new Cookie("token", "0123456789"));
        response.send("Set cookies ..");
    &#125;);

    app.Listen(8080);
&#125;
</code></pre> 
 <h3>支持 sendFile() 方法实现文件下载</h3> 
 <pre><code class="language-cs">
import archttp;

void main()
&#123;
    auto app = new Archttp;

    app.Get("/download", (request, response) &#123;
        response.sendFile("./attachments/avatar.jpg");
    &#125;);

    app.Listen(8080);
&#125;
</code></pre> 
</div> 
<h3>然后..</h3> 
<p>还修复了很多BUG，进一步提升稳定性，也兼容了 Windows 平台的测试，由于作者的开发机系统是 macOS，也就只有一个 Debian 虚拟机用于兼容 Linux 测试，也希望大家能进行体验测试，反馈BUG给作者是非常欢迎的！</p> 
<p>D语言是非常优秀的语言，语法简单程度类似 TypeScript 这种脚本语言，性能又比肩 Rust 和 Golang，希望我能开发一个 ExpressJS 一样使用简单的框架来做 Golang 那么高负载的事！</p>
                                        </div>
                                      
</div>
            