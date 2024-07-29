import type { ISourceOptions } from "@tsparticles/engine";

const particlesOptions: ISourceOptions = {
    background: {
        color: "#000000"
    },
    fullScreen: {
        enable: true,
        zIndex: -1
    },
    particles: {
        number: {
            value: 80,
            density: {
                enable: true,
            }
        },
        color: {
            value: "#ffffff"
        },
        shape: {
            type: "circle"
        },
        opacity: {
            value: 0.5,
            animation: {
                enable: false,
                speed: 1,
                sync: false
            }
        },
        size: {
            value: 3,
            animation: {
                enable: false,
                speed: 1,
                sync: false
            }
        },
        links: {
            enable: true,
            distance: 150,
            color: "#ffffff",
            opacity: 0.4,
            width: 1
        },
        move: {
            enable: true,
            speed: 3,
            direction: "none",
            outModes: "out",
            attract: {
                enable: false,
                rotate: {
                    x: 600,
                    y: 1200
                }
            }
        }
    },
    interactivity: {
        detectsOn: "canvas",
        events: {
            onHover: {
                enable: true,
                mode: "repulse"
            },
            onClick: {
                enable: true,
                mode: "push"
            },
            resize: {
                enable: true,
                delay: 0.5
            }
        },
        modes: {
            grab: {
                distance: 400,
                links: {
                    opacity: 1
                }
            },
            bubble: {
                distance: 400,
                size: 40,
                duration: 2,
                opacity: 8,
            },
            repulse: {
                distance: 200,
                duration: 0.4
            },
            push: {
                quantity: 4
            },
            remove: {
                quantity: 2
            }
        }
    },
    detectRetina: true
};

export default particlesOptions;