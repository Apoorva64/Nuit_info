let canvas = document.getElementsByTagName("canvas")[0];
let ctx = canvas.getContext('2d');
ctx.canvas.width  = window.innerWidth;
ctx.canvas.height = window.innerHeight;
let dx=270,dy=460;
let ex=1100,ey=460;
let inc=5;
let move=true;
let bras_down=false;
let easter_eggs=false;
canvas.addEventListener('click', event => {
  let tx = event.x - canvas.offsetLeft;
  let ty = event.y - canvas.offsetTop;
  if(tx >= 0 && tx <= canvas.width && ty>= 0 && ty <= canvas.height)
  {
      if(tx >= 40 && tx <= 140 && ty >= 220 && ty <= 320)
      {
          move=!move;
          if(!move)
          {
              if(dx >= 270 && dx<=470)
              {
                  bras_down=true;
                  document.location="rescue_list/";
              }
              else if(dx >= 490 && dx<=690)
              {
                  bras_down=true;
                  document.location="rescuer_list/";
              }
              else if(dx >= 710 && dx<=910)
              {
                  bras_down=true;
                  document.location="rescue_boat_list/";
              }
              else if(dx >= 930 && dx<=1130)
              {
                  bras_down=true;
                  document.location="quote_list/";
              }

              if(dx > 470 && dx < 490)
              {
                  bras_down=true;
                  easter_eggs=true;
              }
              else if(dx > 690 && dx < 710)
              {
                  bras_down=true;
                  easter_eggs=true;
              }
              else if(dx > 910 && dx < 930)
              {
                  bras_down=true;
                  easter_eggs=true;
              }
          }
          else
          {
              bras_down=false;
          }
      }
  }
});
var img_cnt=0;
let img = new Image();
img.addEventListener('load', function() {
    img_cnt++;
}, false);
img.src = "/static/img/bark.png";
let img2 = new Image();
img2.addEventListener('load', function() {
    img_cnt++;
}, false);
img2.src = "/static/img/perso.png";
let img3 = new Image();
img3.addEventListener('load', function() {
    img_cnt++;
}, false);
img3.src = "/static/img/Array.jpg";

function draw() {
    if(img_cnt >= 3) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'rgb(51,255,252)';
        ctx.fillRect(0, 0, canvas.width, 480);
        ctx.fillStyle = 'rgb(6,12,137)';
        ctx.fillRect(0, 280, canvas.width, 200);
        if(!bras_down) {
            ctx.strokeStyle = 'rgb(255,12,137)';
            ctx.beginPath();
            ctx.moveTo(115, 270);
            ctx.lineTo(180, 240);
            ctx.stroke();
            ctx.strokeStyle = 'rgb(255,255,255)';
            ctx.beginPath();
            ctx.moveTo(180, 240);
            ctx.lineTo(300, 300);
            ctx.stroke();
        }
        else
        {
            ctx.strokeStyle = 'rgb(255,12,137)';
            ctx.beginPath();
            ctx.moveTo(115, 270);
            ctx.lineTo(130, 200);
            ctx.stroke();
            ctx.strokeStyle = 'rgb(255,255,255)';
            ctx.beginPath();
            ctx.moveTo(130, 200);
            ctx.lineTo(dx, dy-50);
            ctx.stroke();
        }

        ctx.fillStyle = 'rgb(0,0,0)';
        ctx.fillRect(270, 330, 200, 100);
        ctx.font = '28px serif';
        ctx.fillStyle = 'rgb(255,255,255)';
        ctx.fillText(l1, 298, 358);
        ctx.fillStyle = 'rgb(0,0,0)';
        ctx.fillRect(490, 330, 200, 100);
        ctx.font = '28px serif';
        ctx.fillStyle = 'rgb(255,255,255)';
        ctx.fillText(l2, 518, 358);
        ctx.fillStyle = 'rgb(0,0,0)';
        ctx.fillRect(710, 330, 200, 100);
        ctx.font = '28px serif';
        ctx.fillStyle = 'rgb(255,255,255)';
        ctx.fillText(l3, 738, 358);
        ctx.fillStyle = 'rgb(0,0,0)';
        ctx.fillRect(930, 330, 200, 100);
        ctx.font = '28px serif';
        ctx.fillStyle = 'rgb(255,255,255)';
        ctx.fillText(l4, 958, 358);


        ctx.drawImage(img, 40, 290);
        ctx.drawImage(img2, 40, 235);
        if(easter_eggs)
        {
            ctx.drawImage(img3, ex, ey);
            ey = ey * Math.cos(ey);
            ex = ex * Math.cos(ex);
        }
        ctx.strokeStyle = 'rgb(255,0,0)';
        ctx.fillStyle = 'rgb(255,0,0)';
        ctx.beginPath();
        ctx.moveTo(dx, dy);
        ctx.lineTo(dx+20, dy-20);
        ctx.lineTo(dx+40, dy);
        ctx.lineTo(dx, dy);
        ctx.fill();
        if(move) {
            dx = dx + inc;
            if (dx >= 1100) {
                inc -= 5;
            } else if (dx < 260) {
                inc += 5;
            }
        }
    }
}

setInterval(draw, 10);