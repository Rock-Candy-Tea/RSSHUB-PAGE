
---
title: '剑指offer之算法篇（上）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3876'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 18:27:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=3876'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本篇主要谈谈面试中比较头疼的一个点：<code>算法</code></p>
<p>随着技术发展进入深水区，包括前端在内的程序员都躲不了算法这一关，今天主要结合自己研究算法的一些心得，和大家探讨下如何通过算法练习提高自身的技术水平，更轻松的应对面试和日常工作中难题。</p>
<h3 data-id="heading-0">算法和数据结构</h3>
<p>学习算法前，需要将数据结构的知识好好回顾下，比如：堆，栈，数组，字符串，树，链表，图。要掌握这些数据结构的基本特征和操作，特定算法很多就是基于这些结构之上的一些组合</p>
<p>快速提升算法能力的核心就是要学会：分类</p>
<p>算法题千变万化，核心的思想都是可罗列的，排除干扰因素，掌握核心才是你需要训练的。接下来，我们看看常见的算法思想都要哪些，以及怎么快速掌握它们：</p>
<ul>
<li>滑动窗口</li>
<li>动态规划</li>
<li>回溯</li>
<li>递归</li>
<li>贪心算法</li>
</ul>
<h4 data-id="heading-1">滑动窗口</h4>
<p>滑动窗口使用双指针解决问题，所以一般也叫双指针算法，因为两个指针间形成一个窗口，一般用于解决数组，字符串，链表问题。</p>
<p>滑动窗口的核心就是如何移动左右或快慢两个指针来获取结果，经典例题：</p>
<h5 data-id="heading-2">三数之和</h5>
<blockquote>
<p>给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。</p>
</blockquote>
<p>解两数之和的时候，我们通过单指针移动和map表记录已读取的值来求解。到三数之和的时候，单指针就力不从心了。</p>
<p>首先我们对数组进行排序处理，快排的时间复杂度为O(nlogn)</p>
<p>抛开边界情况的处理，核心逻辑就是进行数组遍历，对于每次遍历的起始点 i，如果 nums[i] > 0 则直接跳过，因为数组排序后是递增的，后面的和只会永远大于 0；否则进行窗口滑动，先形成三个点 [i, i+1, n-1]，这样保持 i 不动，不断包夹后两个数字即可，只要它们的和大于 0，就将第三个点左移（数字会变小），否则将第二个点右移（数字会变大），其中第二个和第三个数就是滑动窗口，当两个指针相遇时，则本轮滑动结束</p>
<pre><code class="copyable">var threeSum = function(nums) &#123;
    let res = [];
    if(!nums || nums.length < 3) return res;

    nums.sort((a, b) => a - b);

    for(let i = 0, length = nums.length; i < length - 2; i++)&#123;
        let cur = nums[i];
        if(cur > 0) break;
        if(i > 0 && cur === nums[i - 1]) continue;

        let left = i+1;
        let right = length - 1;
    
        while(left < right)&#123;
            let sum = cur + nums[left] + nums[right];
            if(sum === 0)&#123;
                res.push([cur,nums[left],nums[right]]);
                while(nums[left] === nums[left + 1]) left++;
                while(nums[right] === nums[right - 1]) right--;
                left++;
                right--;
            &#125;
            if(sum > 0)&#123;
                right--;
            &#125;
            if(sum < 0)&#123;
                left++;
            &#125;
        &#125;
    &#125;

    return res;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">环形链表</h5>
<blockquote>
<p>给定一个链表，判断链表中是否有环。要求：空间复杂度 O(1)</p>
</blockquote>
<p>说实话第一次看到这道题时，如果能想到快慢指针的解法，绝对是相当聪明的，因为必须要有知识迁移的能力。想象学校在开运动会，相信每次都有一个跑的最慢的同学，慢到被最快的同学追了一圈。</p>
<p>解题思路就是快慢指针分别跑，只要相遇则判定为环形链表，否则不是环形链表</p>
<pre><code class="copyable">var hasCycle = function(head) &#123;
    let fast = head;
    let slow = head;

    while(fast && fast.next)&#123;
        fast = fast.next.next;
        slow = slow.next;

        if(fast === slow)&#123;
            return true;
        &#125;
    &#125;

    return false;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个思考点就是快慢指针的速度应该怎么指定，如果你直接看题解，肯定知道慢指针走一步，快指针每次走两步，但是为什么呢，快指针每次走三步不可以么。</p>
<p>这就跟快排用二分法，而不是三分法一个道理，原因是二分可以用最小的 “深度”将数组切割为最小粒度。那么同理，快慢指针中，慢指针要想被尽快追上，速度可能最好是快指针的一半</p>
<p>但用一半的慢速是最快的相遇方式吗？不一定，举一个例子，假设链表是完美环形，一共有 [1,6] 共 6 个节点，那么慢指针一次走 1 步，快指针一次走 2 步，那么一共是 [2,3] [3,5] [4,1] [5,3] [6,5] [1,1] 共走 6 步，但如果快指针一次走 3 步呢？一共是 [2,4] [3,1] [4,4] 3 步。这么说一般速度不一定最优？其实不是的，计算机在链表寻址时，节点访问的消耗也要考虑进去，后者虽然看上去更快，但其实访问链表 next 的次数更多，对计算机来说，还不如第一种来得快。
所以准确来说，不是快指针比慢指针快一倍速度，而是慢指针一次走一步，快指针一次走两步最优，因为相遇时，总移动步数最少。</p>
<p>关于使用滑动窗口的问题还有很多，特别是字符串的什么子问题/子结构，要掌握某类解题算法和思想，一定要进行针对性的训练，不能东一枪西一枪，到时候基本全忘记了</p>
<h4 data-id="heading-4">动态规划</h4>
<blockquote>
<p>用动态规划来解的题大部分属于中级以上的题，动态规划灵活多变，非常锻炼脑力和思维</p>
</blockquote>
<p>动态规划与暴力求解不同的是，动态规划需要根据前面子问题的解，推倒出下一步的最优解。所以动态规划可解问题需同时满足以下三个特点：</p>
<ol>
<li>存在最优子结构</li>
<li>存在重复子问题</li>
<li>无后效性</li>
</ol>
<p><strong>存在最优子结构</strong></p>
<blockquote>
<p>子问题的最优解可以推导出全局最优解</p>
</blockquote>
<p>什么是子问题？比如寻路算法中，走完前几步就是相对于走完全程的子问题，必须保证走完全程的最短路径可以通过走完前几步推导出来，才可以用动态规划。寻找最优子结构就是建立动态转移方程的过程，是动态规划中最核心的。</p>
<p><strong>存在重复子问题</strong></p>
<blockquote>
<p>同一个子问题在不同场景下存在重复计算</p>
</blockquote>
<p>这个是动态规划与暴力解法的关键区别，动态规划之所以性能高，是因为 不会对重复子问题进行重复计算，算法上一般通过缓存计算结果或者自底向上迭代的方式解决，但核心是这个场景要存在重复子问题。</p>
<p>典型例子是斐波那契数列，对于 f(3) 与 f(4)，都要计算 f(1) 与 f(2)，因为 f(3) = f(2) + f(1)，而 f(4) = f(3) + f(2) = f(2) + f(1) + f(2)。</p>
<p><strong>无后效性</strong></p>
<blockquote>
<p>前面的选择不会影响后面的游戏规则</p>
</blockquote>
<p>我们使用动态规划求解的问题都具备无后效性，所以可能大家对这个不是很理解，反过来理解一下，什么场景存在后效性呢？</p>
<p>就是你当前的选择影响了后续的结果，人生的职业规划就具有后效性，高考后你选择去复读还是打工，对你以后的人生结果就产生了天翻地覆的变化。不影响结果的选择有哪些呢，比如找零问题中，我当前选择1块钱，还是5块钱，并不影响最后我需要支付的金额总数。背包问题中，我选择的物品多重，不影响最后背包的整体质量大小</p>
<p>动态规划的最难点是如何在复杂的关系中，构建出状态转移方程得到递推关系，接下来用实际例题体会下</p>
<h5 data-id="heading-5">最大子序和</h5>
<blockquote>
<p>给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和</p>
</blockquote>
<blockquote>
<p>输入：nums = [-2,1,-3,4,-1,2,1,-5,4]</p>
</blockquote>
<blockquote>
<p>输出：6</p>
</blockquote>
<blockquote>
<p>解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。</p>
</blockquote>
<p>现在开始构造状态转移方程，使用dp(i)表示以第 i 个字符串结尾的最大和，那么 dp(i-1) 就是以第 i-1 个字符串结尾的最大和，而且此时 dp(i-1) 已经算出来了，那么 dp(i) 怎么推导就清楚了。</p>
<p>因为数组是连续的，所以 dp(i) 要么是 dp(i-1) + nums[i]，要么就直接是 nums[i]，所以选择哪种，取决于前面的 dp(i-1) 是否是正数，<strong>因为以 i 结尾一定包含 nums[i]，所以 nums[i] 不管是正还是负，都一定要带上</strong>。 所以容易得知，dp(i-1) 如果是正数就连起来，否则就不连。
状态转移方程为：</p>
<ul>
<li>dp(i) = dp(i-1) + nums[i] 如果 dp(i-1) > 0。</li>
<li>dp(i) = nums[i] 如果 dp(i-1) <= 0。</li>
</ul>
<pre><code class="copyable">var maxSubArray = function(nums) &#123;
    let n = nums.length;
    let dp = new Array(n);
    dp[0] = nums[0];

    let max = nums[0];
    for (let i = 1; i < n; i++) &#123;
        dp[i] = Math.max(dp[i- 1] + nums[i], nums[i]);
        max = Math.max(max, dp[i]);
    &#125;

    return max;
&#125;;

//然后，发现 dp[i] 只和上一个状态（dp[i-1]）有关，这样就可以只维护一个变量 sum，sum代表了dp[i - 1]，小于0则直接舍弃 保存上一个状态即可。优化空间后是这样的：

var maxSubArray = function(nums) &#123;
    let sum = 0;
    let res = [];
    let max = nums[0];

    for(let i = 0; i < nums.length; i++)&#123;
        if(sum < 0)&#123;
             sum = nums[i];
        &#125;else&#123;
            sum += nums[i];
        &#125;

        max = Math.max(max, sum);
    &#125;
    
    return max;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">打家劫舍</h5>
<blockquote>
<p>你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。</p>
</blockquote>
<blockquote>
<p>给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。</p>
</blockquote>
<blockquote>
<p>输入：[1,2,3,1]</p>
</blockquote>
<blockquote>
<p>输出：4</p>
</blockquote>
<blockquote>
<p>解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。偷窃到的最高金额 = 1 + 3 = 4 。</p>
</blockquote>
<p>这属于非字符串类动态规划问题，由于不能同时打劫相邻的房屋，所以对于 dp(i)，要么为了打劫 i-1 而不打劫第 i 间，或者打劫 i-2 和第 i 间，取这两种终态的收益最大值即可，即 dp(i) = max(dp(i-1), dp(i-2) + coins[i])</p>
<pre><code class="copyable">var rob = function(nums) &#123;
    const len = nums.length;
    if(len === 0)
        return 0;
    const dp = new Array(len + 1);
    dp[0] = 0;
    dp[1] = nums[0];
    for(let i = 2; i <= len; i++) &#123;
        dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i-1]);
    &#125;
    return dp[len];
&#125;;

//由于dp[i]的推倒只依赖前两项的值，进行空间优化后

var rob = function(nums) &#123;
    if(nums.length === 1) return nums[0];
    let prev = Math.max(nums[0], nums[1]);
    let next = nums[0];
    let i = 1;
    let length = nums.length;

    while(i++ < length - 1)&#123;
        let temp = Math.max(prev, next + nums[i]);
        next = prev;
        prev = temp;
    &#125;

    return prev;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>动态规划的核心就是定义清楚状态，即dp(i) 是什么，然后从复杂的关系中，推倒出状态转移方程。背包问题作为最经典的动态规划案例，很值得大家去研究研究</p>
<p>限于篇幅有限，先介绍了滑动窗口和动态规划算法，下篇中再去聊聊回溯，递归，贪心算法该如何去求解，算法训练要以专项练习，不可随心所欲，掌握了常见思想方法后，遇见具体问题，然后进行分析拆解找到适合的求解方法，这也是算法的乐趣所在。</p>
<h3 data-id="heading-7">关于刷题（leetcode）</h3>
<p>提到算法，大家肯定首先想到leetcode，大部分人都或多或少的在上面练习过一些。关于leetcode的定位，许多人褒贬不一，有人甚至把他比作《葵花宝典》，逼着江湖上每个人都要去自宫。</p>
<p>leetcode提供的大量算法案例确实非常适合进行算法学习，既然你要拿到心仪大厂的offer，那么你就只能按照人家的要求证明自己了，至于这种考核方式合不合理，就交给行业去思考吧，我们只需要让自己在任何规则下都能脱颖而出。</p></div>  
</div>
            