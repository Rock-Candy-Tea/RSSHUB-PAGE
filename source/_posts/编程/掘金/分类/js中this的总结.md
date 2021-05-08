
---
title: 'js中this的总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7859'
author: 掘金
comments: false
date: Fri, 07 May 2021 19:56:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=7859'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言：</h3>
<p>js中this问题是学习前端基础的重要部分，如果想要扎实自己的基础，这块硬骨头就必须啃掉~<br>在js实际开发过程中我们一定要搞清楚this的指向以及更改this的指向，高效的完成开发任务。</p>
<h2 data-id="heading-1">this指向分类</h2>
<p>为了能够一眼看出this指向的是什么，我们需要确定它的绑定规则是哪个？this有以下五种规则分类：</p>
<ul>
<li>默认绑定</li>
<li>隐式绑定</li>
<li>显示绑定</li>
<li>new绑定</li>
<li>箭头函数this绑定</li>
</ul>
<h3 data-id="heading-2">默认绑定</h3>
<p>第一种是无绑定状态也就是默认绑定状态，经常是独立的函数中会使用到</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;
foo();<span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面函数就应用了this的默认绑定,foo()前面没有调用它的对象，在非严格模式foo()函数会挂载在window上所以函数中的this指向的是全局对象window。在严格模式下禁止了this关键字指向全局对象,this指向undefined，undefined上没有this对象，会抛出错误。</p>
<h3 data-id="heading-3">隐式绑定</h3>
<p>考虑调用位置是否有调用的对象，如果有会指向调用对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;
<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>:foo
&#125;
obj.foo();<span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为调用foo的时候前面加上了obj，所以隐式绑定会把函数调用中的this绑定到这个上下文对象，也就是obj,所以this.a 和obj.a是一样的
但是，你需要记住一句话：<code>this永远指向最后调用它的那个对象</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;
<span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>:foo
&#125;
<span class="hljs-keyword">var</span> obj2 = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">3</span>,
    <span class="hljs-attr">obj1</span>:obj1
&#125;
obj2.obj1.foo();<span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上文代码执行结果是2，因为this指向最后调用它的那个对象，即obj1。</p>
<pre><code class="copyable">在使用隐式绑定的时候，有一个常见的问题，就是会出现隐式丢失
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">隐式丢失</h4>
<p>隐式丢失是什么意思呢？其实就是被<code>隐式绑定</code>的函数丢失绑定对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a)
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-string">"hello"</span>
<span class="hljs-keyword">var</span> obj = &#123;
<span class="hljs-attr">a</span>: <span class="hljs-string">"obj"</span>,
<span class="hljs-attr">fn</span>: fn
&#125;
<span class="hljs-keyword">var</span> demo = obj.fn; <span class="hljs-comment">//函数别名</span>
demo() <span class="hljs-comment">//???</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家觉得这段代码最终控制台打印的是什么？<br>
执行结果为，控制台打印了hello<br>
为什么呢？<br>
因为demo只是绑定了fn函数的引用，因此demo只是一个函数的调用，应用了默认绑定绑定到了全局对象，该情况很容易出现在回调函数上，例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baz</span>(<span class="hljs-params">fn</span>)</span>&#123;
    fn()
&#125;
<span class="hljs-keyword">var</span> obj = &#123;
    <span class="hljs-attr">a</span>:<span class="hljs-number">2</span>,
    <span class="hljs-attr">foo</span>:foo
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-string">'我是全局对象的a'</span>;
baz(obj.foo);<span class="hljs-comment">//我是全局对象的a</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">参数传递其实就是一种隐式赋值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一种比较特殊的情况就是定时器</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a)
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-string">"hello"</span>
<span class="hljs-keyword">var</span> obj = &#123;
<span class="hljs-attr">a</span>: <span class="hljs-string">"obj"</span>,
<span class="hljs-attr">fn</span>: fn
&#125;
<span class="hljs-built_in">setTimeout</span>(obj.fn,<span class="hljs-number">0</span>); <span class="hljs-comment">//hello</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>setTimeout</code>第一个参数是传入回调函数，obj.fn被当做一个函数进行绑定，可以理解为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setTimeout</span>(<span class="hljs-params">fn,delay</span>)</span>&#123;
<span class="hljs-comment">//等待delay毫秒后执行</span>
fn() <span class="hljs-comment">//obj.fn</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">显示绑定</h3>
<p>所谓显示，是因为你可以直接指定this的绑定对象，我们可以借助apply,call,bind等方法</p>
<p>apply和call作用一样，只是传参的方式不同，都会执行对应的函数，但是bind不一样，它不会执行，需要手动去调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a);
&#125;
<span class="hljs-keyword">var</span> obj = &#123;
  <span class="hljs-attr">a</span>:<span class="hljs-number">2</span>,
&#125;

foo.call(obj);<span class="hljs-comment">//2</span>
foo.apply(obj);<span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，依然无法解决丢失绑定的问题，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello,'</span>, <span class="hljs-built_in">this</span>.name);
 &#125;
 <span class="hljs-keyword">var</span> per = &#123;
     <span class="hljs-attr">name</span>: <span class="hljs-string">'mengyun'</span>,
     <span class="hljs-attr">sayHi</span>: sayHi
 &#125;
 <span class="hljs-keyword">var</span> name = <span class="hljs-string">'anna'</span>;
 <span class="hljs-keyword">var</span> Hi = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>) </span>&#123;
     fn();
 &#125;
 Hi.call(per, per.sayHi); <span class="hljs-comment">//Hello, anna</span>
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是我们可以给fn也硬绑定this，就可以解决这个问题</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello,'</span>, <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-keyword">var</span> per = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'mengyun'</span>,
    <span class="hljs-attr">sayHi</span>: sayHi
&#125;
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'anna'</span>;
<span class="hljs-keyword">var</span> Hi = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">fn</span>) </span>&#123;
    fn.call(<span class="hljs-built_in">this</span>);
&#125;
Hi.call(per, per.sayHi); <span class="hljs-comment">//Hello, mengyun</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>原因：因为per被绑定到Hi函数中的this上，fn又将这个对象绑定给了sayHi的函数。这时，sayHi中的this指向的就是per对象。</p>
<p>其实我更愿意用冒充来描述这个过程，Hi冒充per，拥有了per的一些方法和属性，然后传入的fn是per.sayHi这个函数如果不通过绑定的话还是默认指向了全局对象window所以输出‘anna',所以需要在进行一次冒充，把当前的方法冒充指向Hi，然后Hi指向的优势per，所以最后输出‘mengyun’。</p>
<p>上面代码用bind可以改写成：(bind在你不知道的js（上）中就是被归为硬绑定)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello,'</span>, <span class="hljs-built_in">this</span>.name);
&#125;
<span class="hljs-keyword">var</span> per = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'mengyun'</span>,
    <span class="hljs-attr">sayHi</span>: sayHi
&#125;
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'anna'</span>;
<span class="hljs-keyword">var</span> Hi = sayHi.bind(per);
Hi.call(per, per.sayHi); <span class="hljs-comment">//Hello, mengyun</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">绑定例外</h4>
<p>如果把null或者undefined作为绑定对象传入call,apply,bind,这些值往往会被忽略，实际应用的是默认绑定规则：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj= &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'mengyun'</span>
&#125;
<span class="hljs-keyword">var</span> name = <span class="hljs-string">'Anna'</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bar</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
&#125;
bar.call(<span class="hljs-literal">null</span>); <span class="hljs-comment">//Anna</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">new绑定</h3>
<p>js跟其他语言不一样，没有类，所以我们可以用构造函数来模拟类
使用new来调用函数，会自动执行下面的操作：</p>
<p>创建一个全新的对象
这个对象会被执行[[Prototype]]连接
这个新对象会绑定到函数调用的this
如果函数没有返回其他对象，那么返回这个新对象，否则返回构造函数返回的对象</p>
<h4 data-id="heading-8">手写一个new</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_new</span>(<span class="hljs-params">fn,...args</span>)</span>&#123;
  <span class="hljs-comment">//1、创建一个空对象</span>
  <span class="hljs-comment">//2、这个对象的 __proto__ 指向 fn 这个构造函数的原型对象</span>
  <span class="hljs-keyword">var</span> obj = <span class="hljs-built_in">Object</span>.create(fn.prototype);
  <span class="hljs-comment">//3、改变this指向</span>
  <span class="hljs-keyword">var</span> res = fn.apply(obj,args);
  <span class="hljs-comment">// 4. 如果构造函数返回的结果是引用数据类型，则返回运行后的结果,否则返回新创建的 obj</span>
  <span class="hljs-keyword">if</span> ((res!==<span class="hljs-literal">null</span> && <span class="hljs-keyword">typeof</span> res == <span class="hljs-string">"object"</span>) || <span class="hljs-keyword">typeof</span> res == <span class="hljs-string">"function"</span>) &#123;
      <span class="hljs-keyword">return</span> res;
  &#125;
  <span class="hljs-keyword">return</span> obj;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们用new来绑定一下this</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">name</span>)</span>&#123;
 <span class="hljs-built_in">this</span>.name = name;
&#125;
<span class="hljs-keyword">var</span> per = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">'mengyun'</span>);
<span class="hljs-built_in">console</span>.log(per.name);<span class="hljs-comment">//mengyun</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时per已经被绑定到Person调用中的this上</p>
<h3 data-id="heading-9">优先级</h3>
<p>我们先介绍前四种this绑定规则，那么问题来了，如果一个函数调用存在多种绑定方法，this最终指向谁呢？这里我们直接先上答案，this绑定优先级为：</p>
<p><code>显式绑定 > 隐式绑定 > 默认绑定 </code></p>
<p><code>new绑定 > 隐式绑定 > 默认绑定</code></p>
<p>为什么显式绑定不和new绑定比较呢？因为不存在这种绑定同时生效的情景，如果同时写这两种代码会直接抛错，所以大家只用记住上面的规律即可。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'听风是风'</span>;
&#125;;
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'行星飞行'</span>
&#125;
<span class="hljs-keyword">let</span> echo = <span class="hljs-keyword">new</span> Fn().call(obj);<span class="hljs-comment">//报错 call is not a function</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么我们结合几个例子来验证下上面的规律，首先是显式大于隐式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//显式>隐式</span>
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'行星飞行'</span>,
    <span class="hljs-attr">fn</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;
&#125;;
obj1 = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'时间跳跃'</span>
&#125;;
obj.fn.call(obj1);<span class="hljs-comment">// 时间跳跃</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次是new绑定大于隐式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//new>隐式</span>
obj = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'时间跳跃'</span>,
    <span class="hljs-attr">fn</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'听风是风'</span>;
    &#125;
&#125;;
<span class="hljs-keyword">let</span> echo = <span class="hljs-keyword">new</span> obj.fn();
echo.name;<span class="hljs-comment">//听风是风</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">箭头函数的this</h3>
<p>ES6的箭头函数是另类的存在，为什么要单独说呢，这是因为箭头函数中的this不适用上面介绍的四种绑定规则。</p>
<p>准确来说，箭头函数中没有this，<code>箭头函数的this指向取决于外层作用域中的this，外层作用域或函数的this指向谁，箭头函数中的this便指向谁。</code>有点吃软饭的嫌疑，一点都不硬朗，我们来看个例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;;
&#125;
<span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'听风是风'</span>
&#125;;
<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'时间跳跃'</span>
&#125;;
<span class="hljs-keyword">let</span> bar = fn.call(obj1); <span class="hljs-comment">// fn this指向obj1</span>
bar.call(obj2); <span class="hljs-comment">//听风是风</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为啥我们第一次绑定this并返回箭头函数后，再次改变this指向没生效呢？</p>
<p>前面说了，箭头函数的this取决于外层作用域的this，fn函数执行时this指向了obj1，所以箭头函数的this也指向obj1。除此之外，箭头函数this还有一个特性，那就是<code>一旦箭头函数的this绑定成功，也无法被再次修改，</code>有点硬绑定的意思。</p>
<p>当然，箭头函数的this也不是真的无法修改，我们知道箭头函数的this就像作用域继承一样从上层作用域找，因此我们可以修改外层函数this指向达到间接修改箭头函数this的目的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name);
    &#125;;
&#125;;
<span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'听风是风'</span>
&#125;;
<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'时间跳跃'</span>
&#125;;
fn.call(obj1)(); <span class="hljs-comment">// fn this指向obj1,箭头函数this也指向obj1</span>
fn.call(obj2)(); <span class="hljs-comment">//fn this 指向obj2,箭头函数this也指向obj2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">总结</h3>
<ul>
<li>那么到这里，对于this的五种绑定场景就全部介绍完毕了，如果你有结合例子练习下来，我相信你现在对于this的理解一定更上一层楼了。</li>
<li>那么通过本文，我们知道默认绑定在严格模式与非严格模式下this指向会有所不同。</li>
<li>我们知道了隐式绑定与隐式丢失的几种情况，并简单复习了作用域链与原型链的区别。</li>
<li>相对隐式绑定改变的不可见，我们还介绍了显式绑定以及硬绑定，简单科普了call、apply与bind的区别，并提到当绑定指向为null或undefined时this会指向全局（非严格模式）。</li>
<li>我们介绍了new绑定以及new一个函数会发生什么。</li>
<li>最后我们了解了不太合群的箭头函数中的this绑定，了解到箭头函数的this由外层函数this指向决定，并有一旦绑定成功也无法再修改的特性。</li>
<li>希望在面试题中遇到this的你不再有所畏惧，到这里，本文结束。</li>
</ul></div>  
</div>
            