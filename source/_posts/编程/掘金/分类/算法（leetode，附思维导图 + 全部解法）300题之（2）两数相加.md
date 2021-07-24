
---
title: '算法（leetode，附思维导图 + 全部解法）300题之（2）两数相加'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf443e18ce14de1b1b9da2074576d2d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 01:24:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf443e18ce14de1b1b9da2074576d2d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">标题：算法（leetode，附思维导图 + 全部解法）300题之（2）两数相加</h1>
<h1 data-id="heading-1">一 题目描述</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cf443e18ce14de1b1b9da2074576d2d~tplv-k3u1fbpfcp-zoom-1.image" alt="题目描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1240108bfc5346c2bc46cebd3f6c453c~tplv-k3u1fbpfcp-zoom-1.image" alt="题目描述" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d7878f9bae84d0e91aab8341d03fb4f~tplv-k3u1fbpfcp-zoom-1.image" alt="题目描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">二 解法总览（思维导图）</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32937d323b4b4119ab000d21896e76ca~tplv-k3u1fbpfcp-zoom-1.image" alt="思维导图" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">三 全部解法</h1>
<h3 data-id="heading-4">1 方案1</h3>
<p>1)代码：</p>
<pre><code class="copyable">var addTwoNumbers = function(l1, l2) &#123;
    // 获取链表所代表的值
    const getValueByLink = (link) => &#123;
        let resVal = 0
            // weight表示当前位置的权重，10的“整幂倍”
            weight = 1;
        while (link) &#123;
            resVal += (link.val * weight);
            // 权重乘10，链表位置往后走
            weight *= 10;
            link = link.next;
        &#125;
        return resVal;
    &#125;

    const val_1 = getValueByLink(l1),
        val_2 = getValueByLink(l2);
    let sum = val_1 + val_2;

    // 根据sum值不断遍历、将相应的位置值放入 curLink 里
    // 若 sum = 807 ，则 resLink = [7, 0, 8]
    const resLink = curLink = new ListNode(sum % 10);
    sum = parseInt(sum/10);
    while (sum) &#123;
        // curLink不断放当前sum值的“个位数值”。sum不断赋成parseInt(sum/10)
        curLink.next = new ListNode(sum % 10);
        curLink = curLink.next;
        // 别错写成 sum /= 10，漏了 parseInt ！！
        sum = parseInt(sum/10);
    &#125;

    return resLink;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2 方案2</h3>
<p>1)代码：</p>
<pre><code class="copyable">var addTwoNumbers = function(l1, l2) &#123;
    let resArr = [],
        // carry 是否有进位（其值范围一定是 [0, 1]）
        carry = 0;

    // 1）不断往后拉2个链表
    while (l1 && l2) &#123;
        resArr.push((l1.val + l2.val + carry) % 10);
        carry = parseInt((l1.val + l2.val + carry) / 10);

        l1 = l1.next;
        l2 = l2.next;
    &#125;
    // 2）判断l1、l2 长度情况。谁长就继续“往后拉”谁
    let tmpLink = l1 ? l1 : l2;
    while (tmpLink) &#123;
        resArr.push((tmpLink.val + carry) % 10);
        carry = parseInt((tmpLink.val + carry) / 10);
        tmpLink = tmpLink.next;
    &#125;
    // 3）最后1位可能有进位 —— 需要继续放
    if (carry) &#123;
        resArr.push(carry);
    &#125;
    // 因为 两个非空 的链表，遍历 resArr 将相应位置上的值放到 resLink 即可
    // resLink 是返回的“链表头”，curLink 用于存放“遍历所取到的值”
    let resLink = curLink = new ListNode(resArr[0]),
        i = 1,
        l = resArr.length;
    while (i < l) &#123;
        curLink.next = new ListNode(resArr[i]);
        curLink = curLink.next;
        i++;
    &#125;

    return resLink;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3 方案3（方案2的优化版：不用 resArr 中间变量，直接存链表里、节约内存开销）</h3>
<p>1)代码：</p>
<pre><code class="copyable">var addTwoNumbers = function(l1, l2) &#123;
    let resLink = curLink = null,
        // carry 是否有进位（其值范围一定是 [0, 1]）
        carry = 0;

    // 1）不断往后拉2个链表
    while (l1 && l2) &#123;
        const tmpVal = (l1.val + l2.val + carry) % 10;
        carry = parseInt((l1.val + l2.val + carry) / 10);
        // resLink 为 null，需初始化！
        if (!resLink) &#123;
            resLink = curLink = new ListNode(tmpVal);
        &#125; else &#123;
            curLink.next = new ListNode(tmpVal);
            curLink = curLink.next;
        &#125;

        l1 = l1.next;
        l2 = l2.next;
    &#125;
    // 2）判断l1、l2 长度情况。谁长就继续“往后拉”谁
    let tmpLink = l1 ? l1 : l2;
    while (tmpLink) &#123;
        curLink.next = new ListNode((tmpLink.val + carry) % 10);
        curLink = curLink.next;
        carry = parseInt((tmpLink.val + carry) / 10);
        tmpLink = tmpLink.next;
    &#125;
    // 3）最后1位可能有进位 —— 需要继续放
    if (carry) &#123;
        curLink.next = new ListNode(carry);
        curLink = curLink.next;
    &#125;

    return resLink;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4 方案4（递归）</h3>
<p>1)代码：</p>
<pre><code class="copyable">var addTwoNumbers = function(l1, l2) &#123;
    // “一般递归的特点”：
    // 1 2种实现 —— dfs（深度优先搜索） 和 bfs（广度优先搜索）
    // 2 3个核心
    // 1）确定返回值得类型及其含义
    // 2）确定递归的出口条件及对应的值
    // 3）递归处理的函数体
    const dfs = (l1, l2, carry) => &#123;
        // 其实可以简写成 if (!l1 && !l2 && !carry)。
        // 1）下面3行是递归出口
        if (l1 === null && l2 === null && carry === 0) &#123;
            return null;
        &#125;

        // 2）下面7-8行是递归处理的函数体
        // 此时必定是 l1、l2或carry中存在“真值”（即有 非null 或 非0 值）
        const val_1 = l1 ? l1.val : 0,
            val_2 = l2 ? l2.val : 0,
            next_1 = l1 ? l1.next : null,
            next_2 = l2 ? l2.next : null,
            sum = (val_1 + val_2 + carry);

        let resLink = new ListNode(sum % 10);
        // 边界：别漏了 parseInt ，别的语言也需可直接 sum/10 ！
        resLink.next = dfs(next_1, next_2, parseInt(sum/10));

        // “本次递归”的返回值
        return resLink;
    &#125;

    return dfs(l1, l2, 0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            