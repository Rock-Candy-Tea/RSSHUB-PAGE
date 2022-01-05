
---
title: 'fd 8.3.0 发布，find 替代方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=982'
author: 开源中国
comments: false
date: Wed, 05 Jan 2022 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=982'
---

<div>   
<div class="content">
                                                                    
                                                        <p>fd 是一个在文件系统中寻找条目的程序。它是 find 的一个简单、快速和用户友好的替代品。虽然它的目标不是支持 find 的所有强大功能，但它为大多数的使用情况提供了合理的默认值。</p> 
<p>fd 8.3.0 发布，更新内容如下：</p> 
<h3>性能改进</h3> 
<ul> 
 <li>带有颜色的输出现在明显更快了</li> 
 <li>如果输出没有进入 TTY，那么现在写到 stdout 的内容是缓冲的。这提高了当 fd 的输出被输送到另一个程序或文件中时的性能</li> 
 <li>文件元数据现在在需要它的不同过滤器之间被缓存起来，减少了使用多个过滤器时 <code>stat</code> 系统调用的次数</li> 
</ul> 
<h3>功能</h3> 
<ul> 
 <li>当使用单线程时，不要对来自 <code>--exec</code> 的命令输出进行缓冲</li> 
 <li>增加新的 <code>-q, --quiet</code> 标志</li> 
 <li>增加新的 <code>--no-ignore-parent</code> 标志</li> 
 <li>增加新的 <code>--batch-size</code> 标志</li> 
 <li>增加对立的命令行选项</li> 
 <li>在 <code>LS_COLORS</code> 中增加对更多文件系统指标的支持</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>总是显示搜索结果的 <code>./</code> 前缀，除非输出是 TTY 或者设置了 <code>-strip-cwd-prefix</code></li> 
 <li>在 MSYS 中设置默认的路径分隔符为 <code>/</code></li> 
 <li>fd 不能搜索 RAM 磁盘下的文件</li> 
 <li>fd 在 Windows 上不显示替代的驱动器</li> 
 <li>正确处理对已满设备的写入错误</li> 
 <li>在时间函数（ <code>--change-newer-than</code>、 <code>--change-older-than</code>）中使用本地时区</li> 
 <li>在更多的平台上支持 <code>--list-details</code></li> 
 <li>过滤器 <code>--owner</code>、 <code>--size</code> 和 <code>--changed-&#123;within,before&#125;</code> 现在应用于符号链接 本身，而不是链接目标，除非指定了 <code>--follow</code></li> 
</ul> 
<h3>变化</h3> 
<ul> 
 <li>将自定义的 <code>--path-separator</code> 应用于以 <code>--exec(-batch)</code> 和 <code>--list-details</code> 运行的命令</li> 
</ul> 
<h3><strong>其他</strong></h3> 
<ul> 
 <li>文档更新</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsharkdp%2Ffd%2Freleases" target="_blank">https://github.com/sharkdp/fd/releases</a></p>
                                        </div>
                                      
</div>
            