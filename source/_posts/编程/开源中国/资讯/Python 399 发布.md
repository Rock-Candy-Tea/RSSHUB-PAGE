
---
title: 'Python 3.9.9 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3545'
author: 开源中国
comments: false
date: Thu, 25 Nov 2021 09:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3545'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Python 3.9.9 热修复更新已于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpythoninsider.blogspot.com%2F2021%2F11%2Fpython-399-hotfix-release-is-now.html" target="_blank">上周发布</a>，此版本是 3.9 系列的第八个维护版本。</p> 
<p>3.9.9 是作为 Python 3.9.8 中 argparse 回归的热修复更新而在发布日程之外推出的，此问题会导致复杂的命令行工具无法正确识别子命令。详情见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45235" target="_blank">BPO-45235</a>。</p> 
<p>与 3.9.8 相比，这个版本中只有三个其他的错误修复。</p> 
<ul> 
 <li style="text-align:left"> <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45235" target="_blank">bpo-45235</a>：修复了一个 argparse 错误，此错误在处理子解析器的默认参数时引发了回归，使得叶级参数优先于根级参数</p> </li> 
 <li style="text-align:left"> <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45765" target="_blank">bpo-45765</a>：在 importlib.metadata 中，修复对空路径的分布发现 (distribution discovery)</p> </li> 
 <li style="text-align:left"> <p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.python.org%2Fissue45644" target="_blank">bpo-45644</a>: In-place JSON 文件格式化使用<code><span>python3</span><span> </span><span>-m</span><span> </span><span>json.tool</span><span> </span><span>infile</span><span> </span><span>infile</span></code><span>可正常运行，此前</span>会导致文件为空</p> </li> 
</ul> 
<p>具体细节<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2Frelease%2F3.9.9%2Fwhatsnew%2Fchangelog.html" target="_blank">查看更新日志</a>。</p> 
<p>官方表示，如果正在使用的是 Python 3.9.8，强烈建议升级到 3.9.9。</p>
                                        </div>
                                      
</div>
            