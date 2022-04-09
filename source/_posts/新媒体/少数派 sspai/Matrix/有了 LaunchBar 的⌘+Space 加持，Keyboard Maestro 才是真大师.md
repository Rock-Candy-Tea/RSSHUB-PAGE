
---
title: '有了 LaunchBar 的⌘+Space 加持，Keyboard Maestro 才是真大师'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2022/04/05/a69ece4f93468295a3adad01b2d04110.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Wed, 06 Apr 2022 09:45:01 GMT
thumbnail: 'https://cdn.sspai.com/2022/04/05/a69ece4f93468295a3adad01b2d04110.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-0b37afcb><div class="update-wrap" data-v-0b37afcb></div><div class="content wangEditor-txt minHeight" data-v-0b37afcb><h2>缘起</h2><p>LaunchBar 和 Keyboard Maestro 是两个我日常使用最多的效率工具。据 Keyboard Maestro（简称 KM） 在 About 界面显示，两台 Mac 上的 KM分别为我节省了 5 个月和 3 个月时间。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/a69ece4f93468295a3adad01b2d04110.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/a69ece4f93468295a3adad01b2d04110.png" referrerpolicy="no-referrer"></figure><p>我个人应该是自 2016 年起开始使用 KM，感觉这个数字可能只是略有夸张，可以想见本人日常使用的频繁程度。对我个人而言，KM 实如其名，确实是“键盘大师”，其是“大师”，但是有点过于依赖键盘，优缺点都很明显。优点在 KM 有丰富的功能模块，而且可以通过积木式的可视化排列实现几乎无穷的可能，限制你的只是自己的想象力。具体可以看少数派已有的教程，如：</p><span class="ss-linkCard" link-card-href="https://sspai.com/post/36442"> </span><span class="ss-linkCard" link-card-href="https://sspai.com/post/56142"> </span><p>这些文章入门很好，但是涉及到的 KM 功能可能不到全部的 1/3。个人觉得 KM 最为有用的是可以<strong>感知系统环境</strong>，如剪切板是否改变及其内容，当前软件名称、窗口位置和大小、用户的输入等等。KM 的缺点在其唤起较为困难，虽然 KM 的 Macro 启动方式（<a href="https://wiki.keyboardmaestro.com/Triggers" target="_blank">trigger</a>）已经很丰富，如可以通过热键、剪切板改变、Status_Menu 等，此外还有在 Macro Group 介面可以设置 Palette（一个根据当前软件判断是否弹出的列出了所有 Macro 的界面）。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/e5c15b092b81a64fbfc0bebfa6e991ce.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/e5c15b092b81a64fbfc0bebfa6e991ce.png" referrerpolicy="no-referrer"><figcaption>KM 官网列出的 Trigger 以及一个 Palette 示例</figcaption></figure><p>以上提到的启动方式在 Macro 比较少时还算方便，当 Macro 较多时想找到想要的就会力不从心，如果设置的热键过多，难免记忆混淆；如果依赖 Palette ，每个软件弹出的 Palette 信置不同，需要视觉辅助去寻找，找到后仍需要通过点击或者所提示的热键进行启动。</p><p>LaunchBar 作为启动器软件，其在感知系统环境方面没有 KM 的优势，但在启动方面有先天优势：LaunchBar 系统自带了丰富的 Action、可以对检索到的条目进行二次筛选、其独特的 Retype 机制可以不用删除错误字符即可重新筛选等。因此如果可以通过 LaunchBar 来筛选 KM 的 Macro，将会达到事半功倍的效果。之前已经有部分用户考虑到这个需要，如以上提到的文章“ Keyboard Maestro 入门指南”中就列出了一个 LaunchBar 的 Action，通过这个名为<a href="https://github.com/mlinzner/LaunchBarActions/tree/master/actions/Keyboard%20Maestro" target="_blank">Keyboard Maestro Macros</a><strong> （以下称 KMM）</strong>的 Action，可以检索 KM 中所有可用的 Macro，然后再通过输入字母将需要的 Macro 筛选出，回车以执行。</p><p>KMM 运行流畅，很有实用价值，但其缺点是将所有 KM 的 Macro 都列出来了，这样丧失了 KM 感知系统环境的灵魂。因为多数情况下，我最需要的是只能运行在当前软件下的 Macro，而不是针对其它软件制作的 Macro。此外则是每次需要检索 KM 的 Macro 时，需要通过⌘+Space唤起 LaunchBar，然后输入 “keyboard maestro macros” 或 “kmm”回车进行二次筛选，虽然费时不多，但是打断了思路，影响了流程。受到KMM 启发，想到可以通过制作 LaunchBar 的 Action 和 KM 的 Macro 相配合，实现单击⌘+Space 时唤起 LaunchBar 以供日常启动使用，双击⌘+Space 时就唤起当前软件的 Macro，因考虑到日常工作习惯，有时也需要检索 KM 中其它可用于全局的 Macro（如处理剪切板的 Macro），因此最好是当前软件对应 Macro 在前，全局 Macro 在后，如此岂不美哉。</p><h2>具体实现</h2><h3>Keyboard Maestro 部分</h3><p>KM 部分需要制作三个 Macro。第一个是用于生成所有全局可用的 Macro 属性 JSON 文件的 Macro。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/6f0e3408263e5a9f0f7e6793cbe966e3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/6f0e3408263e5a9f0f7e6793cbe966e3.png" referrerpolicy="no-referrer"><figcaption>用于生成所有全局 Macro 信息JSON的 Macro</figcaption></figure><p>第二个用于生成当前软件可用的 Macro 属性并拼接前面 JSON 文件的 Macro：</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/cbd64b199cf30b0ebed06b72ec2f564e.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/cbd64b199cf30b0ebed06b72ec2f564e.png" referrerpolicy="no-referrer"></figure><p>第三个是用于启动 LaunchBar 的 Macro（命名为 KM to Active LaunchBar），并将 KM 中的变量“LB”传递到 LaunchBar 用于显示和筛选。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/34e1857e518dafb15b7bc5fc1a5e8019.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/34e1857e518dafb15b7bc5fc1a5e8019.png" referrerpolicy="no-referrer"></figure><h3>LaunchBar 部分</h3><p>LaunchBar 需要制一个 Action 用于接收 KM 生成的 JSON 文件并展示出来。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2022/04/05/8e35606342de2f1b467e60bfec2dd7e3.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2022/04/05/8e35606342de2f1b467e60bfec2dd7e3.png" referrerpolicy="no-referrer"><figcaption>LaunchBar 需要制作的 Action</figcaption></figure><p> </p><p> </p><h2>请以你的名字呼唤我</h2><p>到了这里，只需要最后一步：如何设置总击⌘+Space 为打开 LaunchBar，而双击⌘+Space 为激活KM to Active LaunchBar，这时需要另一个软件：<a href="https://karabiner-elements.pqrs.org/" target="_blank">Karabiner-Elements</a>。</p><p>Karabiner-Elements 是一个改键软件，但是除了改键之外，还有其他功能，如可以运行 shell 语句。因此可以通过在 Karabiner-Elements 上设置双击时激活KM to Active LaunchBar（KM 上也有双击击活的 trigger，但是如果在KM to Active LaunchBar 的 trigger 中设置为双击 ⌘+Space，无法激活）。</p><span class="ss-linkCard" link-card-href="https://sspai.com/post/42921"> </span><p>在 Karabiner-Elements 的 Complex modifications 中增加一条设置：</p><pre class="language-javascript"><code>&#123;
    "description": "Double Command Spacebar to run shell",
    "manipulators": [
        &#123;
            "conditions": [
                &#123;
                    "name": "count",
                    "type": "variable_if",
                    "value": 1
                &#125;
            ],
            "from": &#123;
                "key_code": "spacebar",
                "modifiers": &#123;
                    "mandatory": [
                        "left_gui"
                    ]
                &#125;
            &#125;,
            "to": [
                &#123;
                    "shell_command": "osascript -e 'tell application \"Keyboard Maestro Engine\" to do script \"KM to Active LaunchBar 的UUID\" with parameter \"Whatever\" ' "
                &#125;
            ],
            "type": "basic"
        &#125;,
        &#123;
            "from": &#123;
                "key_code": "spacebar",
                "modifiers": &#123;
                    "mandatory": [
                        "left_gui"
                    ]
                &#125;
            &#125;,
            "to": [
                &#123;
                    "set_variable": &#123;
                        "name": "count",
                        "value": 1
                    &#125;
                &#125;,
                &#123;
                    "key_code": "spacebar",
                    "modifiers": [
                        "left_gui"
                    ]
                &#125;
            ],
            "to_delayed_action": &#123;
                "to_if_canceled": [
                    &#123;
                        "set_variable": &#123;
                            "name": "count",
                            "value": 0
                        &#125;
                    &#125;
                ],
                "to_if_invoked": [
                    &#123;
                        "set_variable": &#123;
                            "name": "count",
                            "value": 0
                        &#125;
                    &#125;
                ]
            &#125;,
            "type": "basic"
        &#125;
    ]
&#125;
</code></pre><p> </p><p>将第 22 行的 UUID 更改为之前标出的 UUID，即可实现双击激活对应 Macro。</p><p>至此大功基本告成。</p><h2>尾声</h2><p>因为 LaunchBar是通过英文字符、数字等对内容进行筛选，因此需要在 KM中制作 Macro 时标题加上英文，或者拼音缩写等字符。KM 中可以通过名称对 Macro进行排序，具体可见<a href="https://forum.keyboardmaestro.com/t/macro-palette-organizer-v1-3-updated-dec-3-2021/6088">Palette Organizer v1.3 (updated Dec 3, 2021)</a>的说明。</p><hr><p>说明 1：本文基于 macOS Catalina（10.15.7）、Keyboard Maestro（10.0.2）、LaunchBar（6.15）。因为感觉高版本 macOS 没有重要的值得更新的内容，所以没有升级，高版本是否可用，还请自行测试。</p><p>说明 2：以上提到的 Macro 和 LaunchBar Action 可在<a href="https://github.com/jkhnfk/LaunchKeyboardMaestroMacro" target="_blank">此处下载</a>。</p><p> </p><p> </p><p> </p><p> </p><p> </p><p> </p><p> </p></div><div class="update-details-wrap" data-v-0b37afcb></div><!----></div><div style="border:1px solid transparent;" data-v-0b37afcb></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-0b37afcb><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>1</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>0</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-6416" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90%E6%9C%89%E4%BA%86%20LaunchBar%20%E7%9A%84%E2%8C%98%2BSpace%20%E5%8A%A0%E6%8C%81%EF%BC%8CKeyboard%20Maestro%20%E6%89%8D%E6%98%AF%E7%9C%9F%E5%A4%A7%E5%B8%88%E3%80%91%E7%BC%98%E8%B5%B7LaunchBar%E5%92%8CKeyboardMaestro%E6%98%AF%E4%B8%A4%E4%B8%AA%E6%88%91%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E6%9C%80%E5%A4%9A%E7%9A%84%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7%E3%80%82%E6%8D%AEKeyboardMaestro%EF%BC%88%E7%AE%80%E7%A7%B0KM%EF%BC%89%E5%9C%A8Abou%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-9487" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90%E6%9C%89%E4%BA%86%20LaunchBar%20%E7%9A%84%E2%8C%98%2BSpace%20%E5%8A%A0%E6%8C%81%EF%BC%8CKeyboard%20Maestro%20%E6%89%8D%E6%98%AF%E7%9C%9F%E5%A4%A7%E5%B8%88%E3%80%91%E7%BC%98%E8%B5%B7LaunchBar%E5%92%8CKeyboardMaestro%E6%98%AF%E4%B8%A4%E4%B8%AA%E6%88%91%E6%97%A5%E5%B8%B8%E4%BD%BF%E7%94%A8%E6%9C%80%E5%A4%9A%E7%9A%84%E6%95%88%E7%8E%87%E5%B7%A5%E5%85%B7%E3%80%82%E6%8D%AEKeyboardMaestro%EF%BC%88%E7%AE%80%E7%A7%B0KM%EF%BC%89%E5%9C%A8Abou%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            