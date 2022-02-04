
---
title: 'Console NFT 黑客任务6解密'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/cbb561da-7ac1-4a07-957c-49c4eb4ee22b.png'
author: Matters
comments: false
date: Fri, 04 Feb 2022 03:57:11 GMT
thumbnail: 'https://assets.matters.news/embed/cbb561da-7ac1-4a07-957c-49c4eb4ee22b.png'
---

<div>   
<p>这次的Console NFT黑客任务算是蛮有挑战的。解开最后的密语需要用到SQL Injection, web3, solidity, AES128/MD5 解密</p><p>这次任务的网址: <a href="https://console-nft.art/pro_6/" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/</a></p><p>任务要解密4段密码，然后按照这个格式把最终的命令发给Console机器人：/hacker_riddle_part_6_key4-key2-key1-key3</p><h2>SQL Injection进入管理页面</h2><p>网页显示需要登录账号，查了一遍代码，没有藏在代码里面登录密码。那剩下可能就是需要用SQL Injection来破解了</p><p>账号和密码都输入 <code>" or ""="</code></p><figure class="image"><img src="https://assets.matters.news/embed/cbb561da-7ac1-4a07-957c-49c4eb4ee22b.png" data-asset-id="cbb561da-7ac1-4a07-957c-49c4eb4ee22b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>果然顺利进入管理页面</p><figure class="image"><img src="https://assets.matters.news/embed/f4993e55-8532-4e88-8c03-e34c171054ba.png" data-asset-id="f4993e55-8532-4e88-8c03-e34c171054ba" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>在管理页面的To Do List那里，给了找到每个key的提示</p><ul><li>Key1: 登陆你的账号的密码就是Key1</li><li>Key2: 给Hacker转账，转账的Tx ID就是Key2</li><li>Key3: 需要用到web3</li><li>Key4: 登陆你的账号，破解key4</li></ul><figure class="image"><img src="https://assets.matters.news/embed/62adc3b9-b5a8-40f6-82cb-f8c36a5ee5f6.png" data-asset-id="62adc3b9-b5a8-40f6-82cb-f8c36a5ee5f6" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>破解Key1</h2><p>进入管理页面后，来到Gold Club Members的页面: <a href="https://console-nft.art/pro_6/dashboard/members.php" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/dashboard/members.php</a></p><p>按F12，选择Network，然后输入你的id（user_xxxx discord ID最后4位）。点击Network页面的filter.php, 会看到你输入的id的密码（MD5加密的）</p><figure class="image"><img src="https://assets.matters.news/embed/a7d94426-f282-4b3d-b73d-ca804f500c5b.png" data-asset-id="a7d94426-f282-4b3d-b73d-ca804f500c5b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>由于密码是经过MD5加密的，所有你需要通过<a href="https://www.md5online.org/md5-decrypt.html" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://www.md5online.org/md5-decrypt.html</a> 进行解密</p><p>解密成功，获得我的key1: smokey, 也是我账号的登录密码</p><figure class="image"><img src="https://assets.matters.news/embed/a50fe165-0ccf-435a-9604-79f52483349b.png" data-asset-id="a50fe165-0ccf-435a-9604-79f52483349b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>解密Key2</h2><p>上面的解密获得了账号的登录密码，所以回到登陆页面，用上面破解的密码登录我的账号</p><p>登录成功:</p><figure class="image"><img src="https://assets.matters.news/embed/0fcd1cc1-f652-4e56-958b-261a96e179ee.png" data-asset-id="0fcd1cc1-f652-4e56-958b-261a96e179ee" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>登录成功后，到转账页面，要做的是给Hacker转账获得TX ID: <a href="https://console-nft.art/pro_6/dashboard/payment.php" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/dashboard/payment.php</a></p><figure class="image"><img src="https://assets.matters.news/embed/eedb0aed-562e-4935-9a57-4b10627352f9.png" data-asset-id="eedb0aed-562e-4935-9a57-4b10627352f9" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>发送成功后，到转账记录页面查找TX ID: <a href="https://console-nft.art/pro_6/dashboard/history.php" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/dashboard/history.php</a></p><p>TX ID 就是我的Key2, 所有我的Key2是 g145S42N7x</p><figure class="image"><img src="https://assets.matters.news/embed/92a1076c-abdd-4dad-859c-0c1241ad7431.png" data-asset-id="92a1076c-abdd-4dad-859c-0c1241ad7431" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>解密Key3</h2><p>到Key_3页面: <a href="https://console-nft.art/pro_6/dashboard/key_3.php" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/dashboard/key_3.php</a></p><p>显示的是一个合约链接和一个ABI。很明显是让你调用这个合约的getThirdKey函数获得key3</p><figure class="image"><img src="https://assets.matters.news/embed/1ed4cd88-67a5-4d34-8fd7-b5815f74c92f.png" data-asset-id="1ed4cd88-67a5-4d34-8fd7-b5815f74c92f" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>为了方便，写了小工具调用合约查看Key3: <a href="https://replit.com/@ericet/Hacker6Key3#index.js" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://replit.com/@ericet/Hacker6Key3#index.js</a></p><p>点击运行，然后输入你的4位discord ID，我的是8888，给的结果是adult，这就是我的key3</p><figure class="image"><img src="https://assets.matters.news/embed/ac2a2f6c-31c1-4fba-9e71-9341a6367c90.png" data-asset-id="ac2a2f6c-31c1-4fba-9e71-9341a6367c90" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>解密Key4</h2><p>回到Dashboard页面： <a href="https://console-nft.art/pro_6/dashboard/index.php" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://console-nft.art/pro_6/dashboard/index.php</a> 拉到下面，会给你3串字符</p><figure class="image"><img src="https://assets.matters.news/embed/7de016d4-a43f-4c0b-bab3-d44aeb176d17.png" data-asset-id="7de016d4-a43f-4c0b-bab3-d44aeb176d17" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>把3段字符分别复制到这里进行解密：<a href="https://www.javainuse.com/aesgenerator" rel="noopener noreferrer" target="_blank" class="keychainify-checked">https://www.javainuse.com/aesgenerator</a></p><p>注：secret key那个最多支持16个字符，所以secret key是console_nft_encr</p><p>解密后获得key4: useful</p><figure class="image"><img src="https://matters.news/@ericet/console-nft-%E9%BB%91%E5%AE%A2%E4%BB%BB%E5%8A%A16%E8%A7%A3%E5%AF%86-bafyreibkwddylkb3fn5bdm4ztkxdu2doqwcbxbtpksiyuyutgn6pytzb2a" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>最终命令</h2><p>最终的命令的格式是: /hacker_riddle_part_6_key4-key2-key1-key3</p><p>结合上面解开的4个keys，我的最终命令是：</p><p>/hacker_riddle_part_6_useful-g145S42N7x-smokey-adult</p><p>发送命令给console bot就能获得500个Tokens</p><p>网站还有一个额外的密语，一登录就能看到的: /sqli_hacker</p><p>发送给console bot获得100个tokens</p><figure class="image"><img src="https://assets.matters.news/embed/b3033f00-3093-47f7-b591-527dd18b2c5c.png" data-asset-id="b3033f00-3093-47f7-b591-527dd18b2c5c" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><h2>怎么获得最终命令的格式？</h2><p>是不是好奇怎么获得最终命令的格式的? Dashboard页面底下有个“The Final Key", 里面是一个Solidity合约，但是合约里面有几个语法错误，修改一下部署合约就会获得我上面所说的格式: /hacker_riddle_part_6_key4-key2-key1-key3</p><figure class="image"><img src="https://assets.matters.news/embed/c771e9d1-7207-4485-8c09-f876939cf068.png" data-asset-id="c771e9d1-7207-4485-8c09-f876939cf068" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>如果你有兴趣自己部署合约来获得最终的key，你可以用下面我修改过的合约代码:</p><pre class="ql-syntax" spellcheck="false">pragma solidity ^0.8.0;


contract HackerRiddlePart6_Final_Key &#123;
    
        function finalKey(string memory key_1, string memory key_2, string memory key_3, string memory key_4) public pure returns (string memory) &#123;

        string[5] memory json;

        json[0] = string(
            abi.encodePacked('/hacker_riddle_part_6_')
        );

        json[1] = string(
            abi.encodePacked(key_4, "-")
        );
        json[2] = string(
            abi.encodePacked(key_2, "-")
        );

        json[3] = string(
            abi.encodePacked(key_1, "-")
        );
        json[4] = string(
            abi.encodePacked(key_3)
        );

        string memory result = 
            string(
                abi.encodePacked(
                    json[0],
                    json[1],
                    json[2],
                    json[3],
                    json[4]
                )
        );

        return string(abi.encodePacked(result));
    &#125;

&#125;
</pre><p><br></p>  
</div>
            