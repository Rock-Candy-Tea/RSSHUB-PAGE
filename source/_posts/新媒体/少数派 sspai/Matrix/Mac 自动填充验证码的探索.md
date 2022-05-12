
---
title: 'Mac 自动填充验证码的探索'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://picsum.photos/400/300?random=1478'
author: 少数派 sspai
comments: false
date: Mon, 09 May 2022 02:07:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=1478'
---

<div>   
<div class="articleWidth-content" data-v-6dd0eb6a><div class="update-wrap" data-v-6dd0eb6a></div><div class="content wangEditor-txt minHeight" data-v-6dd0eb6a><h2>背景</h2><p>智能手机发展到 2022 年了，不管使用的是 Android 还是 iOS ，当我们收到短信验证码之后，手机会自动提取出其中的验证码并复制出来，如果给的权限够多，它甚至可以帮你自动填充到你正要输入的地方，只是不同系统之间会有些许差别。</p><p>这是我们都已知且习惯的操作。</p><p><i>当然，验证码作为当前越来越重要的一种安全验证工具，允许软件如此自由获取到验证码是一件非常危险的事情，所以最好不要允许系统外的第三方后台联网输入法来读取它。</i></p><p>但是，如果你使用的是桌面设备，那如何将手机收到的验证码自动在桌面设备上填充呢？</p><h2>探索</h2><p>众所周知，如果恰好同时使用了 Mac 与 iPhone，这个操作 Apple 也已经为你做好了（部分）。</p><p>参考<a href="https://support.apple.com/zh-cn/HT208386">将 iPhone 中的短信/彩信转发到 iPad、iPod touch 或 Mac。</a></p><p>当手机收到短信时将会自动同步到同一个 Apple ID 登录的 Mac 上面。</p><p>如果你使用的正好是 Mac 自带的 Safari 浏览器来填充验证码，恭喜你，你不用做任何操作，你将可以在 Safari 上面点一下直接填充手机收到的验证码。</p><h2>延伸</h2><p>由于 Apple 的隐私限制，在 Safari 之外比如 Chrome 等 Apple 生态外的软件内我们是无法如此方便地填充验证码的。</p><p>咋办，有人和我一样懒吗？</p><p>有人用 <a href="https://www.ohtipi.com/">ohtipi</a> 方案，但是好像收费而且仅仅限制在浏览器内。</p><p>也有其他脚本方案的。</p><p><a href="https://bokunlin.github.io/2021/07/11/Mac-%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%8A%A8%E5%A4%8D%E5%88%B6%E6%89%8B%E6%9C%BA%E9%AA%8C%E8%AF%81%E7%A0%81">Bokun 的方案</a> 是做定时器每分钟跑一次，这种不高频的操作做定时器后台一直跑，感觉有点过了，我参考做了个适合我的手动方案。</p><h3>大致原理</h3><p>Mac 收到的信息内容会存储在 <code>/Users/$&#123;Your Name&#125;/Library/Messages/chat.db</code> 这个文件内，通过脚本读取最近 60 秒的一条信息内容，如果有验证码信息，通过正则筛选出其中的验证码，并复制到剪贴板，成功与否都给出一条系统通知。</p><h3>步骤</h3><p>在你喜欢的地方新建一个 shell 脚本文件（比如 <code>/Users/$&#123;Your Name&#125;/Shells/AutoCheckCode.sh</code>，文件内容在文末），给此文件授予当前用户读与写的权限（选中文件 ⌘+I）。</p><p>测试一下此脚本是否正确，使用系统自带终端或者 iTerm， cd 到存放上一步文件的目录内，执行 <code>./AutoCheckCode.sh</code>，成功与否都将收到一条提示。到这一步，后面只需要考虑如何以最快速的方式执行这个脚本。</p><p><i>需要注意无论使用自带终端、快捷指令、自动操作、或者 iTerm 等执行此脚本，都需要到系统偏好设置-安全与隐私-隐私-完全磁盘访问权限，打开对应软件的权限。</i></p><p>Mac 上快速执行脚本有很多方式，我也都进行了尝试。</p><ul><li>考虑使用 Mac 新版本的快捷指令，运行 Shell 脚本，报错放弃。👎🏻</li><li>使用 Mac 的自动操作编写一个快速操作，然后到系统偏好设置-键盘-快捷键-服务-通用，将刚刚写的操作配置一个快捷键，看起来完美。可是运行发现必须要自动操作这个 APP 在前台才能成功，放弃。👎🏻</li><li>使用自动操作创建一个应用程序，程序内选择运行 shell 脚本，脚本内容为 <code>sh /Users/$&#123;Your Name&#125;/Shells/AutoCheckCode.sh</code>，保存此应用至 Mac 的应用程序目录之内，名称看个人喜欢，比如「复制验证码.app」。同时记得给这个应用完全磁盘访问权限。👍🏻</li></ul><p>此时相当于你已经开发打包并安装了一个 Mac 的应用程序，虽然它很简单。</p><p>触发这个程序的方式那就更多了，Alfred、HapiGo、Raycast，甚至手动点击一下也是可以的，当 Mac 收到短信的时候，执行一下应用即可。</p><h2>脚本内容</h2><pre class="language-shell"><code>#!/bin/bash

echo "starting to check code";
  # 路径中的 dufu 记得改成自己电脑的名字
  # 通过 Sqlite3 查 1 条 iMessage 最近 60 秒收到消息（iMessage 收到消息的时间可能有延迟，这里实际冗余多了 2 秒）
  #! /Users/dufu/Library/Messages/chat.db
  #！这个 DB 文件和目录记得给开权限，默认是不给读的。
  result=$(sqlite3 /Users/dufu/Library/Messages/chat.db 'SELECT text FROM message WHERE datetime(date/1000000000 + 978307200,"unixepoch","localtime") > datetime("now","localtime","-60 second") ORDER BY date DESC LIMIT 1;')

  name="验证码";

  # 看下最近有没有收到消息
  if [ ! $result ]; then
      echo "latest not receive code messsages";
      osascript -e "display notification \"最近60秒未收到验证码！\" with title \"提示\"   ";
      return
  fi

#   如果短信中包含验证码则取前 4-6 个数字
  if [[ "$result" =~ "$name" ]]; then
      code=`echo $result | grep -o "[0-9]\&#123;4,6\&#125;"`;
      echo "code is $code";
      # 将获取到的数字输出到剪贴板
      echo "$code" | pbcopy;

      # 发个系统通知，展示内容，同时提醒你可以 Command + v 粘贴了。
      osascript -e "display notification \"$code\" with title \"验证码已复制\"";
  fi</code></pre><h2>题外</h2><p>另外也可以使用 Mac 的脚本编辑器，输入以下 AppleScript（我使用了 iTerm），<strong>保存时文件格式选择应用程序</strong>。</p><pre class="language-python"><code>tell application "iTerm"
activate
create window with default profile command "sh /Users/dufu/Shells/AutoCheckCode.sh"
end tell</code></pre><p>如果觉得创建的这个 APP 图标不好看，可以复制一张图片，在访达里选中这个应用，按 ⌘+I，选中应用图标 ⌘+V，将你的应用图标替换。</p><p><br> </p></div><div class="update-details-wrap" data-v-6dd0eb6a></div><!----></div><div style="border:1px solid transparent;" data-v-6dd0eb6a></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6dd0eb6a><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>13</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>5</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-7187" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90Mac%20%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85%E9%AA%8C%E8%AF%81%E7%A0%81%E7%9A%84%E6%8E%A2%E7%B4%A2%E3%80%91%E8%83%8C%E6%99%AF%E6%99%BA%E8%83%BD%E6%89%8B%E6%9C%BA%E5%8F%91%E5%B1%95%E5%88%B02022%E5%B9%B4%E4%BA%86%EF%BC%8C%E4%B8%8D%E7%AE%A1%E4%BD%BF%E7%94%A8%E7%9A%84%E6%98%AFAndroid%E8%BF%98%E6%98%AFiOS%EF%BC%8C%E5%BD%93%E6%88%91%E4%BB%AC%E6%94%B6%E5%88%B0%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81%E4%B9%8B%E5%90%8E%EF%BC%8C%E6%89%8B%E6%9C%BA%E4%BC%9A%E8%87%AA%E5%8A%A8%E6%8F%90%E5%8F%96%E5%87%BA%E5%85%B6%E4%B8%AD%E7%9A%84%E9%AA%8C%E8%AF%81%E7%A0%81%E5%B9%B6%E5%A4%8D%E5%88%B6%E5%87%BA%E6%9D%A5%EF%BC%8C%E5%A6%82%E6%9E%9C%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2022%2F05%2F07%2Ff27fb1ce0539566c2cca8663177fca33.jpg%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-5864" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90Mac%20%E8%87%AA%E5%8A%A8%E5%A1%AB%E5%85%85%E9%AA%8C%E8%AF%81%E7%A0%81%E7%9A%84%E6%8E%A2%E7%B4%A2%E3%80%91%E8%83%8C%E6%99%AF%E6%99%BA%E8%83%BD%E6%89%8B%E6%9C%BA%E5%8F%91%E5%B1%95%E5%88%B02022%E5%B9%B4%E4%BA%86%EF%BC%8C%E4%B8%8D%E7%AE%A1%E4%BD%BF%E7%94%A8%E7%9A%84%E6%98%AFAndroid%E8%BF%98%E6%98%AFiOS%EF%BC%8C%E5%BD%93%E6%88%91%E4%BB%AC%E6%94%B6%E5%88%B0%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81%E4%B9%8B%E5%90%8E%EF%BC%8C%E6%89%8B%E6%9C%BA%E4%BC%9A%E8%87%AA%E5%8A%A8%E6%8F%90%E5%8F%96%E5%87%BA%E5%85%B6%E4%B8%AD%E7%9A%84%E9%AA%8C%E8%AF%81%E7%A0%81%E5%B9%B6%E5%A4%8D%E5%88%B6%E5%87%BA%E6%9D%A5%EF%BC%8C%E5%A6%82%E6%9E%9C%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            