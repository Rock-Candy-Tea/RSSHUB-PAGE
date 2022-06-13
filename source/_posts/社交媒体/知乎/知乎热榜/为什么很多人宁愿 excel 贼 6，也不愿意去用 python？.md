
---
title: '为什么很多人宁愿 excel 贼 6，也不愿意去用 python？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://picsum.photos/400/300?random=9007'
author: 知乎
comments: false
date: Sun, 12 Jun 2022 16:27:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=9007'
---

<div>   
Cat Chen的回答<br><br><p data-pid="lGwkpdFq">客户说要什么你就做什么。客户说他要的是 Excel 表格，你就必须给他 Excel 表格。交付时就是一个 xlsx 文件，告诉客户里面所有公式甚至是 VBA 都做好了，如果客户要加数据、该数据可以自行操作，表格会自行更新。客户交钱项目完结。</p><p data-pid="9XphA4XK">如果你用 Python 的话，面对将来客户对数据的调整，你有两个选择：</p><ol><li data-pid="Fkwpiy52">叫用户安装 Python，学习使用命令行，调整数据后就再跑一次同一个脚本刷新数据。客户肯定不接受，就算接受了将来 Python 升级和各种包升级肯定烦死你，你准备好教客户用 virtual environment 了吗？</li><li data-pid="ZjIPR8YM">你叫用户把调整后的数据发给你，你再跑一次脚本，然后把刷新后的结果发给客户。在客户嫌你慢之前你造就被客户来来回回的变动烦死了。</li></ol><p data-pid="lzbvCxzD">凡是用到 Excel 公式和 VBA 的表格，都是动态表格，否则为什么不把所有单元格的值写死？一个 xlsx 文件就能把背后的动态逻辑打包发过去，你为什么要用 Python 来折腾自己呢？真的要用自己选择的语言写数据处理的话，你还是给客户做个带图形化界面的应用程序吧……</p><p data-pid="7NFJ6apm">如果你真的特别特别想要用 Python，我推荐你用 Google Sheet 和 Google Apps Script：</p><a data-draft-node="block" data-draft-type="link-card" href="http://link.zhihu.com/?target=https%3A//developers.google.com/apps-script/api/quickstart/python" class=" external" target="_blank" rel="nofollow noreferrer"><span class="invisible">https://</span><span class="visible">developers.google.com/a</span><span class="invisible">pps-script/api/quickstart/python</span><span class="ellipsis"></span></a><p data-pid="DcNkP65A">在 OAuth 之后你的 Python 脚本能够通过 API 访问整套 Google Sheet 对象模型，喜欢干什么就干什么。</p>  
</div>
            